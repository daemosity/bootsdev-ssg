import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_is_instance(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)
     
    def test_repr_no_values(self):
        node = HTMLNode()
        self.assertEqual(str(node), "HTMLNode(tag=None, value=None, children=None, props=None)")
    
    def test_repr_only_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(str(node), "HTMLNode(tag=p, value=None, children=None, props=None)")
    
    def test_repr_only_value(self):
        node = HTMLNode(value="This is a test")
        self.assertEqual(str(node), "HTMLNode(tag=None, value=This is a test, children=None, props=None)")
    
    def test_repr_only_children(self):
        node = HTMLNode(children=[HTMLNode(tag="<div>")])
        self.assertEqual(str(node), "HTMLNode(tag=None, value=None, children=[HTMLNode(tag=<div>, value=None, children=None, props=None)], props=None)")
        
    def test_repr_only_props(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(str(node), "HTMLNode(tag=None, value=None, children=None, props={'href': 'https://www.google.com'})")
        
    
if __name__ == "__main__":
    unittest.main()