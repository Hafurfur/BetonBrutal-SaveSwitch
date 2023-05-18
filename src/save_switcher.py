import pathlib

from settings import SAVE_LOCATION, SAVE_FILE
import shutil


class Switcher:
    def __init__(self):
        self._create_copay_save_file()

    @staticmethod
    def _create_copay_save_file():
        orig_file_path = pathlib.Path(SAVE_LOCATION, 'copy_save.dat')
        open(orig_file_path, 'a').close()

    @staticmethod
    def new_save():
        orig_file_path = pathlib.Path(SAVE_LOCATION, SAVE_FILE)
        copy_file_path = pathlib.Path(SAVE_LOCATION, 'copy_save.dat')
        shutil.copy2(orig_file_path, copy_file_path)

    @staticmethod
    def load_save():
        orig_file_path = pathlib.Path(SAVE_LOCATION, SAVE_FILE)
        copy_file_path = pathlib.Path(SAVE_LOCATION, 'copy_save.dat')
        shutil.copy2(copy_file_path, orig_file_path)
