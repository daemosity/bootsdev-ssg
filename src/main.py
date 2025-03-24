import sys
from build_functions import copy_source_dir_to_destination_dir, generate_pages_recursive



def main():
    base_path= sys.argv[1] if len(sys.argv) > 1 else "/"
    source_dir = "./static"
    destination_dir = "./docs"
    source_pth = "./content"
    template_pth = "./src/template.html"
    
    copy_source_dir_to_destination_dir(source_dir, destination_dir)
    generate_pages_recursive(source_pth, template_pth, destination_dir, base_path)

main()