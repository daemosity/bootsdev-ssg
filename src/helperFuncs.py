from multiprocessing import Value
from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node:"TextNode"):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(value=text_node.text, tag=None)
        case TextType.BOLD:
            return LeafNode(value=text_node.text, tag="b")
        case TextType.ITALIC:
            return LeafNode(value=text_node.text, tag="i")
        case TextType.CODE:
            return LeafNode(value=text_node.text, tag="code")
        case TextType.LINK:
            return LeafNode(value=text_node.text, tag="a", props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(value="",tag="img", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Not a valid TextType")

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            pattern = re.compile(fr"(?<=\s){delimiter}(?=\w+?\b)|(?<=\b){delimiter}(?=\s)")
            split_line = re.split(pattern, node.text)
            if len(split_line) % 2 == 0:
                raise ValueError(f"Error: Invalid Markdown syntax detected: {node.text}")
            else:
                print(pattern)
                print(split_line)
                generated_nodes = [TextNode(text=match, text_type=text_type) if idx % 2 == 1 else TextNode(text=match, text_type=TextType.TEXT) for idx, match in enumerate(split_line)]
                print(generated_nodes)
                new_nodes.extend(generated_nodes)
    return new_nodes

def extract_markdown_images(text:str) -> list[tuple[str, str]]:
    image_pattern = re.compile("\!\[(\w.+?)\]\((.+?)\)")
    alt_url_tuple_list = image_pattern.findall(text)
    if not alt_url_tuple_list:
        raise ValueError("Markdown invalid for image extraction")
    
    return alt_url_tuple_list

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    link_pattern = re.compile("(?<!\!)\[(\w.+?)\]\((.+?)\)")
    anchor_url_tuple_list = link_pattern.findall(text)
    if not anchor_url_tuple_list:
        raise ValueError("Markdown invalid for image extraction")
    
    return anchor_url_tuple_list
    