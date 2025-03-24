import unittest

from markdown_transformations import extract_title

class TestMarkdownToBlocks(unittest.TestCase):
    def test_returns_h1_of_markdown(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        
        output = extract_title(markdown)
        
        expected_output = "This is a heading"
        self.assertSequenceEqual(output, expected_output)
        
    def test_raises_if_no_h1_header(self):
        markdown = """## This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
if __name__ == "__main__":
    unittest.main()