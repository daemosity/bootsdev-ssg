import unittest

from helperFuncs import extract_markdown_images

class TestLinkExtractor(unittest.TestCase):   
    def test_returns_correct_list_of_tuples(self):
        test_string = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(test_string)
        self.assertSequenceEqual(output, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_returns_only_images_in_text(self):
        test_string = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_images(test_string)
        self.assertSequenceEqual(output, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    
    def test_returns_only_images_with_proper_alt_text(self):
        test_string = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(test_string)
        self.assertSequenceEqual(output, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
if __name__ == "__main__":
    unittest.main()