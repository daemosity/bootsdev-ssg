import os
import shutil

def get_files_in_tree(start_dir):
    if os.path.isfile(start_dir):
        return [start_dir]
    
    dir_lst = os.listdir(start_dir)
    if len(dir_lst) == 0:
        pass
    elif len(dir_lst) == 1:
        new_pth = os.path.join(start_dir, dir_lst[0])
        return [new_pth]
    else:
        filepaths_to_copy = []
        for pth in dir_lst:
            new_pth = os.path.join(start_dir, pth)
            if os.path.isfile(pth):
                filepaths_to_copy.append(new_pth)
            else:
                filepaths_to_copy.extend(get_files_in_tree(new_pth))
        return filepaths_to_copy
            
def copy_files_to_destination(source, destination, file_list):
    for src_path in file_list:
        dest_pth = src_path.replace(source, destination)
        dest_dir = os.path.dirname(dest_pth)
        if os.path.exists(dest_dir):
            print(f"copying {src_path} to {dest_pth}")
            shutil.copy(src_path, dest_pth)
        else:
            print(f"creating the following director(ies): {dest_dir}")
            os.makedirs(dest_dir)
            print(f"copying {src_path} to {dest_pth}")
            shutil.copy(src_path, dest_pth)
            
    

def build_destination_directory(source, destination):
    destination = "./public"
    print(f"checking to see if directories '{source}' (source) or'{destination}' (destination) exists...")
    if not os.path.exists(source):
        print(f"...source dir '{source}' not found, exiting program")
        exit()
    elif os.path.exists(source) and os.path.exists(destination):
        print(f"...directories '{source}' and '{destination}' exist")
        print(f"clearing directory '{destination}'...")
        shutil.rmtree(destination)
        os.mkdir(destination)
    elif os.path.exists(source):
        print(f"...only source dir '{source}' exists")
        print(f"creating new directory '{destination}'...")
        os.mkdir(destination)
    else:
        raise Exception("unknown error occurred")

def main():
    print("running build function")
    source = "./static"
    destination = "./public"
    print("\nbuilding destination directory")
    build_destination_directory(source, destination)
    print("\ncapturing files to copy")
    files_to_copy = get_files_in_tree(source)
    print(f"\ncopying the following files: {files_to_copy}\n")
    copy_files_to_destination(source, destination, files_to_copy)
    print("\ncopy successful!")

main()