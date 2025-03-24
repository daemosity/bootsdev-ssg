import re
from textnode import TextNode, TextType

def get_delimiter_count(delimiter:str, text:str) -> int:
    return text.count(delimiter)

def get_paired_delimiter_indices(delimiter:str, text:str) -> list[int]:
    idx1= text.find(delimiter)
    idx2 = text.find(delimiter, idx1 + 1)
    
    if idx2 == -1:
        idx2 = idx1
        
    if idx1 < 0 or idx2 < 0:
        return None
    
    return idx1, idx2

def contains_valid_delimiters(text:str, delimiter:str) -> bool:
    count = get_delimiter_count(delimiter, text)
    result = get_paired_delimiter_indices(delimiter, text)
    if not (
        result
        and result[1] > result[0] + 1 # Just in case an italic delimiter finds a bold one
        and count % 2 == 0
        ):
        return False
    return True

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        found_match = False
        delim_cpy = delimiter
        try:
            match (True):
                case True if node.text_type != TextType.TEXT:
                    new_nodes = new_nodes + [node]
                    
                case True if delim_cpy not in node.text:
                    new_nodes = new_nodes + [node]
                
                # case True if delim_cpy in node.text and contains_valid_delimiters(node.text, "`"):
                #     found_match = True
                # case True if delim_cpy in node.text and contains_valid_delimiters(node.text, "```"):
                #     found_match = True
                #     delim_cpy = delimiter.replace("```", "`")
                case True if (delim_cpy in node.text and contains_valid_delimiters(node.text, delim_cpy)):
                    found_match = True
                    if delimiter == "**":
                        delim_cpy = r"\*\*"
                    else:
                        delim_cpy = delimiter
                    
                case _:
                    raise ValueError(f"Error: Invalid Markdown syntax detected: {node.text}")
        except Exception as err:
            raise err
        
        if found_match:           
            found_words = re.findall(f"{delim_cpy}(.+?){delim_cpy}", node.text)
            leftover = node.text
            for word in found_words:
                # print(leftover)
                # print(found_words)
                # print(delimiter)
                # print(delim_cpy)
                
                splitting_word = f"{delimiter}{word}{delimiter}"
                first_bit, leftover = leftover.split(splitting_word, maxsplit=1)
            
                initial_nodes = [
                    TextNode(text=first_bit, text_type=TextType.TEXT),
                    TextNode(text=word, text_type=text_type)
                ]
                
                new_nodes += initial_nodes
                
            if leftover != "" or not leftover.isspace():
                new_nodes += [TextNode(text=leftover, text_type=TextType.TEXT)]
    return new_nodes