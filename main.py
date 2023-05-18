from src.save_switcher import Switcher
from src.game_procestion import GameProc


def start():
    switcher = Switcher()
    game = GameProc()
    print(f'1. Copy save file \n2. Load copy save')
    while True:
        inp = input()
        if inp == '1':
            switcher.new_save()
            print(f'Save copy')
        elif inp == '2':
            switcher.load_save()
            print(f'Save load')
            game.game_star()
        else:
            print(f'Wrong input value')


if __name__ == '__main__':
    start()
