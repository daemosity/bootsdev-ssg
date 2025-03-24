import re

from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextType, TextNode
from leafnode import LeafNode
from markdown_transformations import block_to_block_type, extract_markdown_images, extract_markdown_links, markdown_to_blocks, BlockType
from split_nodes_delimiter import split_nodes_delimiter

def text_node_to_html_node(text_node:TextNode) -> LeafNode:
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

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            # print(f"New nodes: {new_nodes}")
        else:
            original_text = node.text
            extracted_links = extract_markdown_images(node.text)
            if not extracted_links:
                new_nodes.append(node)
                # print(f"New nodes: {new_nodes}")
                continue
            
            left_over_text = original_text
            generated_node_list = []
            for alt_text, url in extracted_links:
                [first_part, left_over_text] = left_over_text.split(f"![{alt_text}]({url})",maxsplit=1)
                generated_node_list = generated_node_list + [
                    TextNode(text=first_part, text_type=TextType.TEXT), 
                    TextNode(text=alt_text, text_type=TextType.IMAGE, url=url)
                    ]
                # print(f"generated_node_list: {generated_node_list}")
                
            generated_node_list = generated_node_list + [TextNode(text=left_over_text, text_type=TextType.TEXT)] if left_over_text else generated_node_list
            new_nodes = new_nodes + generated_node_list
            
    return new_nodes

def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            # print(f"New nodes: {new_nodes}")
        else:
            original_text = node.text
            extracted_links = extract_markdown_links(node.text)
            if not extracted_links:
                new_nodes.append(node)
                # print(f"New nodes: {new_nodes}")
                continue
            
            left_over_text = original_text
            generated_node_list = []
            for anchor_text, url in extracted_links:
                [first_part, left_over_text] = left_over_text.split(f"[{anchor_text}]({url})",maxsplit=1)
                generated_node_list = generated_node_list + [
                    TextNode(text=first_part, text_type=TextType.TEXT), 
                    TextNode(text=anchor_text, text_type=TextType.LINK, url=url)
                    ]
                # print(f"generated_node_list: {generated_node_list}")
                
            generated_node_list = generated_node_list + [TextNode(text=left_over_text, text_type=TextType.TEXT)] if left_over_text else generated_node_list
            new_nodes = new_nodes + generated_node_list
            
    return new_nodes

def text_to_textnodes(text:str) -> list[TextNode]:
    
    new_text_node = TextNode(text=text, text_type=TextType.TEXT)
    delimiters_and_types = [("_", TextType.ITALIC), ("**", TextType.BOLD), ("`", TextType.CODE)]
    
    generated_node_list = [new_text_node]
    for delimiter, text_type in delimiters_and_types:
        generated_node_list = split_nodes_delimiter(generated_node_list, delimiter, text_type)
    
    generated_node_list = split_nodes_image(generated_node_list)
    generated_node_list = split_nodes_link(generated_node_list)
    
    return generated_node_list

def block_to_html_parent_node(blocktype:BlockType, markdown_block:str):
    split_markdown = markdown_block.split("\n") if "\n" in markdown_block else [markdown_block]
    match (blocktype):
        
        case BlockType.QUOTE:
            children = []
            for line in split_markdown:
                stripped_text = line.lstrip("> ")
                leaf_nodes = text_to_HTMLchildren([stripped_text])
                children += leaf_nodes
            return ParentNode(tag="blockquote", children=children)
        
        case BlockType.UNORDERED_LIST:
            li_parents = []
            for line in split_markdown:
                if line.startswith("-"):
                    stripped_text = line.lstrip("- ")
                else:
                    stripped_text = line.lstrip("* ")
                leaf_nodes = text_to_HTMLchildren([stripped_text])
                li_parents.append(ParentNode(tag="li", children=leaf_nodes))
                # print(leaf_nodes)
            return ParentNode(tag="ul", children=li_parents)
        
        case BlockType.ORDERED_LIST:
            li_parents = []
            for line in split_markdown:
                [number, text] = line.split(". ", maxsplit=1)
                # print(f"{number=}, {text=}")
                leaf_nodes = text_to_HTMLchildren([text])
                li_parents.append(ParentNode(tag="li", children=leaf_nodes))
            return ParentNode(tag="ol", children=li_parents)
        
        case BlockType.CODE:
            new_line = markdown_block.replace("`", "").strip()
            code_node = TextNode(new_line, text_type = TextType.CODE)
            children = [text_node_to_html_node(code_node)]
            return ParentNode(tag="pre", children=children)
        
        case BlockType.HEADING:
            [heading_hashes, heading_text] = split_markdown[0].split(" ", maxsplit=1)
            num_hashes = heading_hashes.count("#")            
            leaf_nodes = text_to_HTMLchildren([heading_text])
            return ParentNode(tag=f"h{num_hashes}", children=leaf_nodes)
        
        case BlockType.PARAGRAPH:
            leaf_nodes = text_to_HTMLchildren(split_markdown)
            return ParentNode(tag="p", children=leaf_nodes)
        
        case _:
            raise Exception("Not a valid BlockType")

def text_to_HTMLchildren(split_markdown:list[str]) -> list[HTMLNode]:
    textnodes = []
    for text in split_markdown:
        textnodes = textnodes + text_to_textnodes(text)
    
    leafnodes = []
    for node in textnodes:
        leafnodes = leafnodes + [text_node_to_html_node(node)]
    return leafnodes
        

def markdown_document_to_html_parent(markdown:str):
    parent_nodes = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        try:
            parent_node = block_to_html_parent_node(block_type, block.strip())
        except Exception as err:
            print()
            print(block)
            print(block_type)
            print()
            raise err
        parent_nodes.append(parent_node)
    return ParentNode(tag="div", children=parent_nodes)
        
        