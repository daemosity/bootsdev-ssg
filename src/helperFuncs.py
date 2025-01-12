from typing import Text
from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node:"TextNode") -> LeafNode:
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

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
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
    
    return alt_url_tuple_list

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    link_pattern = re.compile("(?<!\!)\[(\w.+?)\]\((.+?)\)")
    anchor_url_tuple_list = link_pattern.findall(text)
    
    return anchor_url_tuple_list

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            print(f"New nodes: {new_nodes}")
        else:
            original_text = node.text
            extracted_links = extract_markdown_images(node.text)
            if not extracted_links:
                new_nodes.append(node)
                print(f"New nodes: {new_nodes}")
                continue
            
            left_over_text = original_text
            generated_node_list = []
            for alt_text, url in extracted_links:
                [first_part, left_over_text] = left_over_text.split(f"![{alt_text}]({url})",maxsplit=1)
                generated_node_list = generated_node_list + [
                    TextNode(text=first_part, text_type=TextType.TEXT), 
                    TextNode(text=alt_text, text_type=TextType.IMAGE, url=url)
                    ]
                print(f"generated_node_list: {generated_node_list}")
                
            generated_node_list = generated_node_list + [TextNode(text=left_over_text, text_type=TextType.TEXT)] if left_over_text else generated_node_list
            new_nodes = new_nodes + generated_node_list
            
    return new_nodes


def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            print(f"New nodes: {new_nodes}")
        else:
            original_text = node.text
            extracted_links = extract_markdown_links(node.text)
            if not extracted_links:
                new_nodes.append(node)
                print(f"New nodes: {new_nodes}")
                continue
            
            left_over_text = original_text
            generated_node_list = []
            for anchor_text, url in extracted_links:
                [first_part, left_over_text] = left_over_text.split(f"[{anchor_text}]({url})",maxsplit=1)
                generated_node_list = generated_node_list + [
                    TextNode(text=first_part, text_type=TextType.TEXT), 
                    TextNode(text=anchor_text, text_type=TextType.LINK, url=url)
                    ]
                print(f"generated_node_list: {generated_node_list}")
                
            generated_node_list = generated_node_list + [TextNode(text=left_over_text, text_type=TextType.TEXT)] if left_over_text else generated_node_list
            new_nodes = new_nodes + generated_node_list
            
    return new_nodes
        
def text_to_textnodes(text:str) -> TextNode:
    new_text_node = TextNode(text=text, text_type=TextType.TEXT)
    delimiters_and_types = [("\*", TextType.ITALIC), ("\*\*", TextType.BOLD), ("`", TextType.CODE)]
    
    generated_node_list = [new_text_node]
    for delimiter, text_type in delimiters_and_types:
        generated_node_list = split_nodes_delimiter(generated_node_list, delimiter, text_type)
    
    generated_node_list = split_nodes_image(generated_node_list)
    generated_node_list = split_nodes_link(generated_node_list)
    
    return generated_node_list

def markdown_to_blocks(markdown:str):
    split_markdown = re.split("\n\n|\n\s+?", markdown)
    filtered_blocks = list(filter(lambda x: not x.isspace(), split_markdown))
    return filtered_blocks

def block_to_block_type(markdown_block:str):
    pass