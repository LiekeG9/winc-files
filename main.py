__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

def clean_cache():
    fDir = os.path.realpath(os.path.dirname(__file__)) + "\cache"
    if os.path.exists(fDir):
        for f in os.listdir(fDir):
            os.remove(os.path.join(fDir, f))
    else:
        os.mkdir(fDir)
    return None

def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zip:
        zip.extractall(cache_dir_path)
    return True

def cached_files():
    fList = []
    fDir = os.path.realpath(os.path.dirname(__file__)) + "\cache"
    if os.path.exists(fDir):
        for f in os.listdir(fDir):
            fList.append(os.path.join(fDir, f))
    return fList

def find_password(list_files):
    for fFile in list_files:
        with open(fFile) as fFileObject:
            fContents = fFileObject.readlines()
            for fLine in fContents:
                if "password" in fLine:
                    x = fLine.find(": ")
                    fPassword = fLine[x+2:].rstrip()
                    return fPassword

# -----------------------------------------------------------------------------------------------
# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def main():
    # opdracht 1
    clean_cache()

    # opdracht 2
    zip_file_path = os.path.realpath(os.path.dirname(__file__)) + "\data.zip"
    cache_dir_path = os.path.realpath(os.path.dirname(__file__)) + "\cache"
    cache_zip(zip_file_path, cache_dir_path)

    # opdracht 3
    print(cached_files())

    # opdracht 4
    print(find_password(cached_files()))
    
if __name__ == "__main__":
    main()
