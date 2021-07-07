__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
path = os.path.dirname(os.path.realpath(__file__))
zip_path = os.path.join(path, 'cache')
zip_files = os.path.join(path, 'data.zip')


def clean_cache():
    if os.path.isdir(zip_path):
        shutil.rmtree(zip_path)  # delete folder/cache
        os.mkdir(zip_path)  # create folder/cache
    else:
        return os.mkdir(zip_path)


# clean_cache()

def cache_zip(file_path: str, cache_dir_path: str):
    clean_cache()
    return shutil.unpack_archive(file_path, cache_dir_path)

#cache_zip(zip_files, zip_path)


def cached_files():
    # fuction will return a list of files in the cache dir
    os.chdir(zip_path)
    for root, dirs, files in os.walk('.'):
        file_list = [os.path.abspath(name) for name in files]

    return file_list


# print(cached_files())


def find_password(cached_files):
    search_pw = "password"
    for i in cached_files:
        f = open(i, "r")
        for line in f:
            if search_pw in line:
                password = line.split(" ")[1].strip()
                return password


print(find_password(cached_files()))
