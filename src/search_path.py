import winreg
import pathlib

def search_steam_loc():
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\WOW6432Node\Valve\Steam')
        steam_path = winreg.QueryValueEx(hkey, 'InstallPath')
    except FileNotFoundError:
        hkey = None
        steam_path = None
        print('Failed to find Steam location')
        return

    winreg.CloseKey(hkey)
    return steam_path[0]

def search_save_loc():
    save_path = pathlib.Path(STEAM_LOCATION, 'userdata').glob('Stats.dat')
    print(f'ff')

    pass