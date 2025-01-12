import unittest

from helperFuncs import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_returns_correct_list_of_tuples(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        
        output = markdown_to_blocks(markdown)
        
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertSequenceEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()