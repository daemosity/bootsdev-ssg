from enum import Enum

TextType = Enum("TextType", ["NORMAL", "BOLD", "ITALIC", "CODE", "LINK", "IMAGES"])

class TextNode:
    def __init__(self, text:str, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: "TextNode"):
        if all([self.text == other.text, self.text_type == other.text_type, self.url == other.url]):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"