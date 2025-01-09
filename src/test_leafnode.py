import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_is_instance(self):
        node = LeafNode(value="This is a leaf Node", tag=None)
        self.assertIsInstance(node, LeafNode)
     
    def test_raise_without_args(self):
        with self.assertRaises(TypeError):
            LeafNode()
    
    def test_raises_if_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode(value=None, tag=None).to_html()
    
    def test_returns_raw_text_if_no_tag(self):
        html_output = LeafNode(value="This is a leaf node", tag=None).to_html()
        self.assertEqual(html_output, "This is a leaf node")
    
    def test_returns_html_if_tag_and_value(self):
        html_output = LeafNode(value="This is a paragraph of text.", tag="p").to_html()
        self.assertEqual(html_output, "<p>This is a paragraph of text.</p>")
        
    def test_returns_tag_value_props_correctly(self):
        html_output = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"}).to_html()
        self.assertEqual(html_output, '<a href="https://www.google.com">Click me!</a>')
    
    def test_repr_with_value_no_tag(self):
        node = LeafNode(value="This is a test", tag=None)
        self.assertEqual(str(node), "LeafNode(tag=None, value='This is a test', props=None)")
    
    def test_repr_with_value_with_tag(self):
        node = LeafNode(value="This is a test", tag='a')
        self.assertEqual(str(node), "LeafNode(tag='a', value='This is a test', props=None)")
        
    def test_repr_only_props(self):
        node = LeafNode(value="This is a test", tag='a', props={"href": "https://www.google.com"})
        self.assertEqual(str(node), "LeafNode(tag='a', value='This is a test', props={'href': 'https://www.google.com'})")

if __name__ == "__main__":
    unittest.main()