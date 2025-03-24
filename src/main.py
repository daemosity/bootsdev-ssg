from build_functions import copy_source_dir_to_destination_dir, generate_pages_recursive



def main():
    source_dir = "./static"
    destination_dir = "./public"
    source_pth = "./content"
    template_pth = "./src/template.html"
    
    copy_source_dir_to_destination_dir(source_dir, destination_dir)
    generate_pages_recursive(source_pth, template_pth, destination_dir)

main()