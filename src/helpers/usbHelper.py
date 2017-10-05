import sys
import os

sys.path.append(os.path.dirname(__file__) + "../")

from custom_exceptions.FileNotFoundException import FileNotFoundException
from custom_exceptions.PendriveDisconnectedException import PendriveDisconnectedException

PENDRIVE_PATH = "/media/pi"

def is_pendrive_connected():
    directories = next(os.walk(PENDRIVE_PATH))[1]
    return len(directories) > 0

def save_txt_file_in_pendrive(file_name, text_to_save):
    file_path = _build_file_path(file_name)

    file_to_save = open(file_path, "w")
    file_to_save.write(text_to_save)
    file_to_save.close()

def open_txt_file_from_pendrive(file_name):
    file_path = _build_file_path(file_name)

    if not os.path.isfile(file_path):
        raise FileNotFoundException()

    return open(file_path, "r")

def _build_file_path(file_name):
    directories = next(os.walk(PENDRIVE_PATH))[1]
    if len(directories) == 0:
        raise PendriveDisconnectedException()
    
    pendrive_name = directories[0]
    return "{}/{}/{}{}".format(PENDRIVE_PATH, pendrive_name, file_name, ".txt")