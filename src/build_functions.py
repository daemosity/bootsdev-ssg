import os
import shutil

from markdown_transformations import extract_title
from node_transformations import markdown_document_to_html_parent

def _get_files_in_tree(start_dir):
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
                filepaths_to_copy.extend(_get_files_in_tree(new_pth))
        return filepaths_to_copy
            
def _copy_files_to_destination(source, destination, file_list):
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

def _build_destination_directory(source, destination):
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

def copy_source_dir_to_destination_dir(source, destination):
    print("running build function")

    print("\nbuilding destination directory")
    _build_destination_directory(source, destination)
    print("\ncapturing files to copy")
    files_to_copy = _get_files_in_tree(source)
    print(f"\ncopying the following files: {files_to_copy}\n")
    _copy_files_to_destination(source, destination, files_to_copy)
    print("\ncopy successful!")

def build_pages(source_dir_path, dest_dir_path, template_path, file_list):
    for src_path in file_list:
        dest_pth = src_path.replace(source_dir_path, dest_dir_path).replace(".md", ".html")
        dest_dir = os.path.dirname(dest_pth)
        if os.path.exists(dest_dir):
            generate_page(src_path, template_path, dest_pth)
        else:
            print(f"creating the following director(ies): {dest_dir}")
            os.makedirs(dest_dir)
            generate_page(src_path, template_path, dest_pth)

def generate_page(from_path, template_path, dest_path):
    missing_filepaths = []
    if not os.path.exists(from_path):
        missing_filepaths.append(from_path)
    if not os.path.exists(template_path):
        missing_filepaths.append(template_path)
        
    if len(missing_filepaths):
        err_message = f"Unable to find files at {', '.join(missing_filepaths)}"
        raise Exception(err_message)
    
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_doc = None
    template_doc = None
    with open(from_path) as f:
        markdown_doc = f.read()
    
    with open(template_path) as t:
        template_doc = t.read()
        
    htmlParent = markdown_document_to_html_parent(markdown_doc)
    html_translation = htmlParent.to_html()
    page_title = extract_title(markdown_doc)
    edited_template = template_doc.replace("{{ Title }}", page_title).replace("{{ Content }}", html_translation)
           
    with open(dest_path, "w") as d:
        d.write(edited_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    missing_filepaths = []
    if not os.path.exists(dir_path_content):
        missing_filepaths.append(dir_path_content)
    if not os.path.exists(template_path):
        missing_filepaths.append(template_path)
    
    if len(missing_filepaths):
        err_message = f"Unable to find files at {', '.join(missing_filepaths)}"
        raise Exception(err_message)
    
    files_to_generate = _get_files_in_tree(dir_path_content)
    build_pages(dir_path_content, dest_dir_path, template_path, files_to_generate)