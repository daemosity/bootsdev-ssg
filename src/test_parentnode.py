import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_is_instance(self):
        node = ParentNode(tag=None, children=None)
        self.assertIsInstance(node, ParentNode)
     
    def test_raise_without_args(self):
        with self.assertRaises(TypeError):
            ParentNode()
    
    def test_raises_if_value_given(self):
        with self.assertRaises(TypeError):
            ParentNode(value="None", tag=None, children=None)

    def test_raises_if_to_html_called_and_tag_none(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[]).to_html()

    def test_raises_if_to_html_called_and_children_none(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="a", children=None).to_html()
            
    def test_to_html_returns_tags_only_if_no_children(self):
        html_output = ParentNode(tag="a", children=[]).to_html()
        self.assertEqual(html_output, f"<a></a>")
    
    def test_to_html_returns_tags_containing_Leaf_children(self):
        html_output = ParentNode(tag="a", children=[LeafNode(tag="b", value="Bold text")]).to_html()
        self.assertEqual(html_output, f"<a><b>Bold text</b></a>")

    def test_to_html_returns_tags_containing_Leaf_children_with_props(self):
        html_output = ParentNode(tag="a", children=[LeafNode(tag="b", value="Bold text", props={"class":"unnecessary"})]).to_html()
        self.assertEqual(html_output, f'<a><b class="unnecessary">Bold text</b></a>')

    def test_to_html_returns_tags_containing_Parent_children(self):
        html_output = ParentNode(tag="a", children=[ParentNode(tag="div", children=[LeafNode(tag="b", value="Bold text")])]).to_html()
        self.assertEqual(html_output, f"<a><div><b>Bold text</b></div></a>") 

    def test_to_html_returns_tags_containing_Parent_children_with_props(self):
        html_output = ParentNode(tag="a", children=[ParentNode(tag="div", children=[LeafNode(tag="b", value="Bold text")], props={"class":"necessary"})]).to_html()
        self.assertEqual(html_output, f'<a><div class="necessary"><b>Bold text</b></div></a>') 
        
if __name__ == "__main__":
    unittest.main()