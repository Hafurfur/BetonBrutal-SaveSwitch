import logging
import pathlib
import os
import subprocess
from settings import STEAM_FLAG, GAME_LOCATION_EXE


class GameProc:
    def __init__(self):
        self.game_loc: str = os.environ['GAME_LOCATION_EXE'] if STEAM_FLAG == 'Y' else GAME_LOCATION_EXE

    def star_game(self):
        game_path = pathlib.Path(self.game_loc, 'BetonBrutal.exe')
        try:
            subprocess.Popen([game_path, 'start'])
        except Exception:
            logging.exception('Failed to start the game')
            raise
        print(f'--> Game load')


if __name__ == '__main__':
    pass
