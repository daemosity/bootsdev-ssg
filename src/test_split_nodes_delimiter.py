import unittest

from helperFuncs import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelim(unittest.TestCase):
    def test_raises_when_no_matching_delimiter(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode(text="This is *incorrect markdown", text_type=TextType.TEXT)], delimiter="\*", text_type=TextType.ITALIC)
        
    def test_raises_when_list_of_nodes_not_given(self):
        node = TextNode(text="This is plain text", text_type=TextType.TEXT)
        with self.assertRaises(TypeError):
            split_nodes_delimiter(node, delimiter="\*", text_type=TextType.ITALIC)
        

    def test_returns_list_unchanged_if_no_Text_TextType(self):
        nodelist = [TextNode(text="This is bold text", text_type=TextType.BOLD), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        transformed_nodelist = split_nodes_delimiter(nodelist, delimiter="\*", text_type=TextType.ITALIC)
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_bold_delimiters_returns_bold_TextNode(self):
        nodelist = [TextNode(text="This is **bold** text", text_type=TextType.TEXT), TextNode(text="This is *italic* text", text_type=TextType.TEXT)]
        transformed_nodelist = split_nodes_delimiter(nodelist, delimiter="\*\*", text_type=TextType.BOLD)
        self.assertSequenceEqual(transformed_nodelist, [TextNode(text="This is ", text_type=TextType.TEXT), TextNode(text="bold", text_type=TextType.BOLD), TextNode(text=" text", text_type=TextType.TEXT), TextNode(text="This is *italic* text", text_type=TextType.TEXT)])

    def test_italic_delimiters_returns_italic_TextNode(self):
        nodelist = [TextNode(text="This is **bold** text", text_type=TextType.TEXT), TextNode(text="This is *italic* text", text_type=TextType.TEXT)]
        transformed_nodelist = split_nodes_delimiter(nodelist, delimiter="\*", text_type=TextType.ITALIC)
        self.assertSequenceEqual(transformed_nodelist, [TextNode(text="This is **bold** text", text_type=TextType.TEXT), TextNode(text="This is ", text_type=TextType.TEXT), TextNode(text="italic", text_type=TextType.ITALIC), TextNode(text=" text", text_type=TextType.TEXT)])

    def test_code_delimiters_returns_code_TextNode(self):
        nodelist = [TextNode(text="This is **bold** text", text_type=TextType.TEXT), TextNode(text="This is `code` text", text_type=TextType.TEXT)]
        transformed_nodelist = split_nodes_delimiter(nodelist, delimiter="`", text_type=TextType.CODE)
        self.assertSequenceEqual(transformed_nodelist, [TextNode(text="This is **bold** text", text_type=TextType.TEXT), TextNode(text="This is ", text_type=TextType.TEXT), TextNode(text="code", text_type=TextType.CODE), TextNode(text=" text", text_type=TextType.TEXT)])
    
        
if __name__ == "__main__":
    unittest.main()