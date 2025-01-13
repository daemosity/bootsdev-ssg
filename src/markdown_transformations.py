from enum import Enum
import re

BlockType = Enum("BlockType", ["PARAGRAPH", "HEADING", "CODE", "QUOTE", "UNORDERED_LIST", "ORDERED_LIST"])

def extract_markdown_images(text:str) -> list[tuple[str, str]]:
    image_pattern = re.compile("\!\[(\w.+?)\]\((.+?)\)")
    alt_url_tuple_list = image_pattern.findall(text)
    
    return alt_url_tuple_list

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    link_pattern = re.compile("(?<!\!)\[(\w.+?)\]\((.+?)\)")
    anchor_url_tuple_list = link_pattern.findall(text)
    
    return anchor_url_tuple_list

def markdown_to_blocks(markdown:str) -> list[str]:
    split_markdown = re.split("\n\n|\n\s+?", markdown)
    filtered_blocks = list(filter(lambda x: not x.isspace(), split_markdown))
    return filtered_blocks

def block_to_block_type(markdown_block:str):   
    match (True):
        case True if re.search("^#{1,6} \w", markdown_block):
            return BlockType.HEADING
        case True if re.fullmatch("^```(?s:.+?)```$", markdown_block):
            return BlockType.CODE
        case True if re.search("(?m:^>)", markdown_block):
            return BlockType.QUOTE
        case True if all([line.startswith("- ") for line in markdown_block.split("\n")]) or all([line.startswith("* ") for line in markdown_block.split("\n")]):
            return BlockType.UNORDERED_LIST
        case True if all([ line.startswith(f"{num + 1}. ") for num, line in enumerate(markdown_block.split("\n"))]):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
        
def extract_title(markdown:str):
    found = re.match("# (.+?)\n", markdown)
    if found:
        return found.group(1)
    else:
        raise ValueError("No h1 header found in document")