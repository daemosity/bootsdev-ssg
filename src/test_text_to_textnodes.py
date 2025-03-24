import unittest

from node_transformations import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):     
    def test_returns_plain_text_if_no_markdown_given(self):
        text = "This is plain text"
        
        result = text_to_textnodes(text)
        
        expected_nodelist = [TextNode(text="This is plain text", text_type=TextType.TEXT)]
        self.assertEqual(result, expected_nodelist)
    
    
    def test_returns_bold_text_if_bold_markdown_given(self):
        text = "This is **bold** text"
        
        result = text_to_textnodes(text)
        
        expected_nodelist = [
            TextNode(text="This is ", text_type=TextType.TEXT), 
            TextNode(text="bold", text_type=TextType.BOLD), 
            TextNode(text=" text", text_type=TextType.TEXT)
            ]
        self.assertEqual(result, expected_nodelist)
    
    def test_returns_italic_text_if_italic_markdown_given(self):
        text="This is _italic_ text"
        
        result = text_to_textnodes(text)
        
        expected_nodelist= [
            TextNode(text="This is ", text_type=TextType.TEXT), 
            TextNode(text="italic", text_type=TextType.ITALIC), 
            TextNode(text=" text", text_type=TextType.TEXT)
            ]
        
        self.assertEqual(result, expected_nodelist)

    def test_returns_code_text_if_code_markdown_given(self):
        text="This is `code` text"
        
        result = text_to_textnodes(text)
        
        expected_nodelist= [
            TextNode(text="This is ", text_type=TextType.TEXT), 
            TextNode(text="code", text_type=TextType.CODE), 
            TextNode(text=" text", text_type=TextType.TEXT)
            ]
        
        self.assertEqual(result, expected_nodelist)
        
    def test_returns_link_text_if_link_markdown_given(self):
        text="This is text with a link [to youtube](https://www.youtube.com/@bootdotdev)"
        
        result = text_to_textnodes(text)
        
        expected_nodelist= [
            TextNode(text="This is text with a link ", text_type=TextType.TEXT), 
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"), 
            ]
        
        self.assertEqual(result, expected_nodelist)
        
    def test_returns_image_text_if_image_markdown_given(self):
        text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        
        result = text_to_textnodes(text)
        
        expected_nodelist= [
            TextNode(text="This is text with a ", text_type=TextType.TEXT), 
            TextNode(text="rick roll", text_type=TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
            ]
        
        self.assertEqual(result, expected_nodelist)
    
    def test_extracts_markdown_correctly(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        result = text_to_textnodes(text)
        
        expected_nodelist = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        
        self.assertEqual(result, expected_nodelist)
        
    def test_extracts_markdown_correctly2(self):
        text = "As we stand at the threshold of this mystical realm, it is clear that _The Lord of the Rings_ is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: _The Lord of the Rings_ reigns supreme as the greatest legendarium our world has ever known."
        
        result = text_to_textnodes(text)
        print(result)
        
        expected_nodelist = [
            TextNode("As we stand at the threshold of this mystical realm, it is clear that ", TextType.TEXT),
            TextNode("The Lord of the Rings", TextType.ITALIC),
            TextNode(" is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: ", TextType.TEXT),
            TextNode("The Lord of the Rings", TextType.ITALIC),
            TextNode(" reigns supreme as the greatest legendarium our world has ever known.", TextType.TEXT)
        ]
        
        self.assertEqual(result, expected_nodelist)
    
        
if __name__ == "__main__":
    unittest.main()