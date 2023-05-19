from src.save_switcher import Switcher
from src.game_procestion import GameProc
from src.search_path import SearchPaths
from settings import STEAM_FLAG
import src.logger


def start():
    if STEAM_FLAG == 'Y':
        SearchPaths.search_path()

    switcher = Switcher()
    game = GameProc()
    print(f'1. Copy save file \n2. Load copy save')
    while True:
        inp = input()
        if inp == '1':
            switcher.new_save()
        elif inp == '2':
            switcher.load_save()
            game.star_game()
        else:
            print(f'Wrong input value')


if __name__ == '__main__':
    start()
