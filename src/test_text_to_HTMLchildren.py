import unittest

from node_transformations import text_to_HTMLchildren
from leafnode import LeafNode

class TestTextToHTMLChildren(unittest.TestCase):     
    def test_transforms_paragraph_markdown_to_leaf_list(self):
        split_markdown = ["This is a paragraph of text. It has some **bold** and _italic_ words inside of it."]
        
        output = text_to_HTMLchildren(split_markdown)
        
        expected_output = [
            LeafNode(value="This is a paragraph of text. It has some ", tag=None),
            LeafNode(value="bold", tag="b"),
            LeafNode(value=" and ", tag=None),
            LeafNode(value="italic", tag="i"),
            LeafNode(value=" words inside of it.", tag=None)
        ]
        self.assertSequenceEqual(output, expected_output)

    def test_transforms_markdown_list_to_leaf_list(self):
        split_markdown = [
            "* This is the **first** list item in a list block",
            "* This is a _second_ list item",
            "* This is a list item with `some code` in it"
            ]
        
        output = text_to_HTMLchildren(split_markdown)
        
        expected_output = [
            LeafNode(value="* This is the ", tag=None),
            LeafNode(value="first", tag="b"),
            LeafNode(value=" list item in a list block", tag=None),
            LeafNode(value="* This is a ", tag=None),
            LeafNode(value="second", tag="i"),
            LeafNode(value=" list item", tag=None),
            LeafNode(value="* This is a list item with ", tag=None),
            LeafNode(value="some code", tag="code"),
            LeafNode(value=" in it", tag=None)
        ]
        self.assertSequenceEqual(output, expected_output)
        
if __name__ == "__main__":
    unittest.main()