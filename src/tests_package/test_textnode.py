import unittest

from ..node_classes.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_is_instance(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsInstance(node, TextNode)
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq_when_url_different(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://reddit.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_when_one_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_when_textType_different(self):
        node = TextNode("This is a text node", TextType.CODE, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertNotEqual(node, node2)
     
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode(This is a text node, BOLD, None)")
    
    def test_typeError_without_textType(self):
        with self.assertRaises(TypeError):
            TextNode("This is a text node")
    
if __name__ == "__main__":
    unittest.main()