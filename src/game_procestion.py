import pathlib
import subprocess
import os
import time

from settings import GAME_LOCATION_EXE, GAME_PROCESS


class GameProc:
    def __init__(self):
        self.subproc = None

    def game_star(self):
        game_path = pathlib.Path(GAME_LOCATION_EXE)
        subprocess.Popen([game_path, 'start'])
        print(f'Game load')


if __name__ == '__main__':
    gg = GameProc()
    # gg.game_star()
