import unittest

from ..markdown_transformations import block_to_block_type
from ..markdown_transformations import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_assigns_heading(self):
        block = "# This is a header"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.HEADING)

    def test_assigns_heading(self):
        block = "###### This is a header"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.HEADING)
    
    def test_assigns_code(self):
        block = """```
This is code
```"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.CODE)

    def test_assigns_quote(self):
        block = "> This is a quote"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.QUOTE)

    def test_assigns_multi_quote(self):
        block = """> This is a quote
>This is its second line
> This is its third line"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.QUOTE)

    def test_assigns_dash_unordered_list(self):
        block = "- This is an unordered list"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_assigns_multi_dash_unordered_list(self):
        block = """- This is an unordered list
- This is item two
- This is item three"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_assigns_star_unordered_list(self):
        block = "* This is an unordered list"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_assigns_multi_star_unordered_list(self):
        block = """* This is an unordered list
* This is item two
* This is item three"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_assigns_ordered_list(self):
        block = "1. This is an ordered list"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.ORDERED_LIST)

    def test_assigns_multi_ordered_list(self):
        block = """1. This is an ordered list
2. This is item two
3. This is item three"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.ORDERED_LIST)

    def test_assigns_paragraph(self):
        block = "This is a paragraph"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_when_too_many_hash(self):
        block = "####### This is a header"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_when_code_without_triple_backticks(self):
        block = """``
This is code
``"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_when_code_missing_closing_backticks(self):
        block = """```
This is code
"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_when_no_space_in_dash_unordered_list(self):
        block = "-This is an unordered list"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_when_no_space_in_star_unordered_list(self):
        block = "*This is an unordered list"
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)
    
    def test_assigns_paragraph_when_mixing_star_and_dash_list(self):
        block = """* This is an unordered list
- This is item two
* This is item three"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_assigns_paragraph_to_incorrectly_incrementing_ordered_list(self):
        block = """1. This is an ordered list
1. This is item two
5. This is item three"""
        
        output = block_to_block_type(block)
        
        self.assertEqual(output, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()