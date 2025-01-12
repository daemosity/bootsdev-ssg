import re

def extract_markdown_images(text:str) -> list[tuple[str, str]]:
    image_pattern = re.compile("\!\[(\w.+?)\]\((.+?)\)")
    alt_url_tuple_list = image_pattern.findall(text)
    
    return alt_url_tuple_list

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    link_pattern = re.compile("(?<!\!)\[(\w.+?)\]\((.+?)\)")
    anchor_url_tuple_list = link_pattern.findall(text)
    
    return anchor_url_tuple_list

def markdown_to_blocks(markdown:str):
    split_markdown = re.split("\n\n|\n\s+?", markdown)
    filtered_blocks = list(filter(lambda x: not x.isspace(), split_markdown))
    return filtered_blocks

def block_to_block_type(markdown_block:str):
    pass