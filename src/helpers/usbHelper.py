import os

PENDRIVE_PATH = "/media/pi"

def is_pendrive_connected():
    directories = next(os.walk(PENDRIVE_PATH))[1]
    return len(directories) > 0

def save_txt_file_in_pendrive(file_name, text_to_save):
    directories = next(os.walk(PENDRIVE_PATH))[1]

    if len(directories) == 0:
        print "No hay ningun pendrive conectado."
        return
    
    pendrive_name = directories[0]
    file_path = "{}/{}/{}{}".format(PENDRIVE_PATH, pendrive_name, file_name, ".txt")

    file_to_save = open(file_path, "w")
    file_to_save.write(text_to_save)
    file_to_save.close()