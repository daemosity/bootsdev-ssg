import unittest

from ..node_classes.parentnode import ParentNode
from ..node_classes.leafnode import LeafNode

from ..node_transformations import markdown_document_to_html_parent

class TestMarkdownDocToHTMLParent(unittest.TestCase):     
    def test_returns_plain_text_if_no_markdown_given(self):
        document = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        output = markdown_document_to_html_parent(document)
        
        expected_output= ParentNode(
            tag="div",
            children = [
                ParentNode( tag="h1", children=[ LeafNode( value="This is a heading", tag=None )]),
                ParentNode( tag="p", children=[
                    LeafNode( value="This is a paragraph of text. It has some ", tag=None ),
                    LeafNode( value="bold", tag="b" ),
                    LeafNode( value=" and ", tag=None ),
                    LeafNode( value="italic", tag="i" ),
                    LeafNode( value=" words inside of it.", tag=None )
                ]),
                ParentNode( tag="ul", children=[
                    ParentNode( tag="li", children=[ LeafNode( value="This is the first list item in a list block", tag=None )]),
                    ParentNode( tag="li", children=[ LeafNode( value="This is a list item", tag=None )]),
                    ParentNode( tag="li", children=[ LeafNode( value="This is another list item", tag=None )]),
                ])
            ]
        )
        self.assertEqual(output, expected_output)

        
if __name__ == "__main__":
    unittest.main()