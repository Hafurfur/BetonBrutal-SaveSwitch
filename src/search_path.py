import logging
import winreg
import pathlib
import os
import traceback


class SearchPaths:
    _steam_loc: str = ''
    _save_loc: str = ''
    _game_loc: str = ''

    @classmethod
    def search_path(cls):
        cls._steam_loc_search()
        cls._save_loc_search()
        cls._game_loc_exe_search()

    @classmethod
    def _steam_loc_search(cls):
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\WOW6432Node\Valve\Steam1')
        except FileNotFoundError:
            logging.exception('Steam not found')
            raise

        try:
            steam_path = winreg.QueryValueEx(hkey, 'InstallPath')
        except FileNotFoundError:
            logging.exception('Steam install path not found')
            raise

        winreg.CloseKey(hkey)

        cls._steam_loc = steam_path[0]
        os.environ['STEAM_LOCATION'] = steam_path[0]

    @classmethod
    def _save_loc_search(cls):
        for root, dirs, files in os.walk(pathlib.Path(cls._steam_loc, 'userdata')):
            if 'Stats.dat' in files and '2330500' in root:
                cls._save_loc = root
                os.environ['SAVE_LOCATION'] = root
                break

        if cls._save_loc == '':
            logging.error('Save file not found')
            raise FileNotFoundError('Save file not found')


    @classmethod
    def _game_loc_exe_search(cls):
        for root, dirs, files in os.walk(pathlib.Path(cls._steam_loc, 'steamapps\common')):
            if 'BetonBrutal.exe' in files:
                cls._game_loc = root
                os.environ['GAME_LOCATION_EXE'] = root
                break

        if cls._game_loc == '':
            logging.error('Game exe not found')
            raise FileNotFoundError('Game exe not found')


if __name__ == '__main__':
    pass
