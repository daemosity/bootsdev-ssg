import unittest

from ..markdown_transformations import extract_markdown_links

class TestLinkExtractor(unittest.TestCase):    
    def test_returns_correct_list_of_tuples(self):
        test_string = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(test_string)
        self.assertSequenceEqual(output, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        
    def test_returns_only_links_in_text(self):
        test_string = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(test_string)
        self.assertSequenceEqual(output, [("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_returns_only_links_with_anchor_text(self):
        test_string = "This is text with a link (https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(test_string)
        self.assertSequenceEqual(output, [("to youtube", "https://www.youtube.com/@bootdotdev")])
        
if __name__ == "__main__":
    unittest.main()