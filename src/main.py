from textnode import TextType, TextNode
from helperFuncs import split_nodes_delimiter

def main():
    print(split_nodes_delimiter([TextNode(text="This is *incorrect* markdown", text_type=TextType.TEXT)], delimiter="*", text_type=TextType.ITALIC))

main()