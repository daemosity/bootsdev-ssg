import unittest

from node_transformations import block_to_html_parent_node, BlockType
from leafnode import LeafNode
from parentnode import ParentNode

class TestBlockToHTMLParentNode(unittest.TestCase):     
    def test_returns_parent_given_markdown_block_and_block_type(self):
        markdown = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        block_type = BlockType.PARAGRAPH
        
        output = block_to_html_parent_node(block_type, markdown)
        
        self.assertIsInstance(output, ParentNode)
        
    def test_transforms_paragraph_block_to_paragraph_parent(self):
        markdown = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        block_type = BlockType.PARAGRAPH
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is a paragraph of text. It has some ", tag=None),
            LeafNode(value="bold", tag="b"),
            LeafNode(value=" and ", tag=None),
            LeafNode(value="italic", tag="i"),
            LeafNode(value=" words inside of it.", tag=None)
        ]
        expected_output = ParentNode(tag="p", children=expected_children)
        self.assertEqual(output, expected_output)


    def test_transforms_header_block_to_header_parent(self):
        markdown = "# This is a header"
        block_type = BlockType.HEADING
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is a header", tag=None),
        ]
        expected_output = ParentNode(tag="h1", children=expected_children)
        self.assertEqual(output, expected_output)


    def test_transforms_lower_level_header_block_to_header_parent(self):
        markdown = "###### This is a header"
        block_type = BlockType.HEADING
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is a header", tag=None),
        ]
        expected_output = ParentNode(tag="h6", children=expected_children)
        self.assertEqual(output, expected_output)

    def test_transforms_code_block_to_pre_code_parent(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        block_type = BlockType.CODE
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [LeafNode(value=
"""This is text that _should_ remain
the **same** even with inline stuff""", tag="code")]
        
        expected_output = ParentNode(tag="pre", children=expected_children)
        self.assertEqual(output, expected_output)
    

    def test_transforms_quote_block_to_quote_parent(self):
        markdown = "> This is a quote"
        block_type = BlockType.QUOTE
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is a quote", tag=None),
        ]
        expected_output = ParentNode(tag="blockquote", children=expected_children)
        self.assertEqual(output, expected_output)

    def test_transforms_multi_quote_block_to_quote_parent(self):
        markdown = """> This is a quote
>This is its second line
> This is its third line"""
        block_type = BlockType.QUOTE
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is a quote", tag=None),
            LeafNode(value="This is its second line", tag=None),
            LeafNode(value="This is its third line", tag=None)
        ]
        expected_output = ParentNode(tag="blockquote", children=expected_children)
        self.assertEqual(output, expected_output)

    def test_transforms_ul_to_ul_parent(self):
        markdown = "- This is an unordered list"
        block_type = BlockType.UNORDERED_LIST
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is an unordered list", tag=None),
        ]
        expected_parents = [
            ParentNode(tag="li", children=expected_children)
        ]
        expected_output = ParentNode(tag="ul", children=expected_parents)
        self.assertEqual(output, expected_output)

    def test_transforms_ul_block_to_ul_parent(self):
        markdown = """* This is an unordered list
* This is item two
* This is item three"""
        block_type = BlockType.UNORDERED_LIST
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_parents = [
            ParentNode(tag="li", children=[LeafNode(value="This is an unordered list", tag=None)]),
            ParentNode(tag="li", children=[LeafNode(value="This is item two", tag=None)]),
            ParentNode(tag="li", children=[LeafNode(value="This is item three", tag=None)]),
        ]
        expected_output = ParentNode(tag="ul", children=expected_parents)
        self.assertEqual(output, expected_output)

    def test_transforms_ol_to_ol_parent(self):
        markdown = "1. This is an ordered list"
        block_type = BlockType.ORDERED_LIST
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_children = [
            LeafNode(value="This is an ordered list", tag=None),
        ]
        expected_parents = [
            ParentNode(tag="li", children=expected_children)
        ]
        expected_output = ParentNode(tag="ol", children=expected_parents)
        self.assertEqual(output, expected_output)

    def test_transforms_ol_block_to_ol_parent(self):
        markdown = """1. This is an ordered list
2. This is item two
3. This is item three"""
        block_type = BlockType.ORDERED_LIST
        
        output = block_to_html_parent_node(block_type, markdown)
        
        expected_parents = [
            ParentNode(tag="li", children=[LeafNode(value="This is an ordered list", tag=None)]),
            ParentNode(tag="li", children=[LeafNode(value="This is item two", tag=None)]),
            ParentNode(tag="li", children=[LeafNode(value="This is item three", tag=None)]),
        ]
        expected_output = ParentNode(tag="ol", children=expected_parents)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()