import unittest

from helperFuncs import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextToHTML(unittest.TestCase):
    def test_raises_when_not_textType(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(TextNode(text="This has no textType", text_type="meh"))
        
    def test_proper_textType_returns_Leaf(self):
        node = TextNode(text="This is plain text", text_type=TextType.TEXT)
        transformed_node = text_node_to_html_node(node)
        self.assertIsInstance(transformed_node, LeafNode)

    def test_textType_Text_returns_raw(self):
        node = TextNode(text="This is plain text", text_type=TextType.TEXT)
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="This is plain text", tag=None, props=None))
    
    def test_textType_bold_returns_bold(self):
        node = TextNode(text="This is bold text", text_type=TextType.BOLD)
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="This is bold text", tag="b", props=None))

    def test_textType_italic_returns_italic(self):
        node = TextNode(text="This is italic text", text_type=TextType.ITALIC)
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="This is italic text", tag="i", props=None))
        
    def test_textType_code_returns_code(self):
        node = TextNode(text="This is code text", text_type=TextType.CODE)
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="This is code text", tag="code", props=None))
        
    def test_textType_link_returns_link(self):
        node = TextNode(text="This is link text", text_type=TextType.LINK, url='example.com')
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="This is link text", tag="a", props={"href":"example.com"}))
        
    def test_textType_image_returns_image(self):
        node = TextNode(text="This is alt text", text_type=TextType.IMAGE, url="example.com")
        transformed_node = text_node_to_html_node(node)
        self.assertEqual(transformed_node, LeafNode(value="", tag="img", props={"src":"example.com", "alt":"This is alt text"}))
    
        
if __name__ == "__main__":
    unittest.main()