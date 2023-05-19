import logging
import pathlib
import os
import shutil
from settings import SAVE_LOCATION, STEAM_FLAG


class Switcher:
    def __init__(self):
        self.save_loc: str = os.environ['SAVE_LOCATION'] if STEAM_FLAG == 'Y' else SAVE_LOCATION
        self._create_copay_save_file()

    def _create_copay_save_file(self):
        try:
            open(pathlib.Path(self.save_loc, 'copy_save.dat'), 'a').close()
        except Exception:
            logging.exception('Failed to create a save copy file')
            raise

    def new_save(self):
        try:
            shutil.copy2(pathlib.Path(self.save_loc, 'Stats.dat'), pathlib.Path(self.save_loc, 'copy_save.dat'))
        except Exception:
            logging.exception('Failed to create a copy of the save')
            raise
        print(f'--> Save copy')

    def load_save(self):
        try:
            shutil.copy2(pathlib.Path(self.save_loc, 'copy_save.dat'), pathlib.Path(self.save_loc, 'Stats.dat'))
        except Exception:
            logging.exception("Couldn't load a copy of the save")
            raise
        print(f'--> Save load')


if __name__ == '__main__':
    pass
