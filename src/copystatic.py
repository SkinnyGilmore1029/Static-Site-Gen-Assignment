from os.path import join,isfile,exists
from os import listdir,mkdir
from shutil import copy



def copy_files_recursive(source_dir_path, dest_dir_path):
    if not exists(dest_dir_path):
        mkdir(dest_dir_path)

    for filename in listdir(source_dir_path):
        from_path = join(source_dir_path, filename)
        dest_path = join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if isfile(from_path):
            copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
