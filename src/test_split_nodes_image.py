import unittest

from helperFuncs import split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodesImage(unittest.TestCase):        
    def test_raises_when_list_of_nodes_not_given(self):
        node = TextNode(text="This is plain text", text_type=TextType.TEXT)
        with self.assertRaises(TypeError):
            split_nodes_image(node)
        

    def test_returns_list_unchanged_if_no_Text_TextType(self):
        nodelist = [
            TextNode(text="This is bold text", text_type=TextType.BOLD), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        
        transformed_nodelist = split_nodes_image(nodelist)
        
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_returns_list_unchanged_Text_has_no_images(self):
        nodelist = [
            TextNode(text="This is regular text", text_type=TextType.TEXT), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        
        transformed_nodelist = split_nodes_image(nodelist)
        
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_generates_correct_nodes_from_single_image(self):
        nodelist = [
            TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", text_type=TextType.TEXT), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        
        transformed_nodelist = split_nodes_image(nodelist)
        
        expected_nodelist = [
            TextNode(text="This is text with a ", text_type=TextType.TEXT), 
            TextNode(text="rick roll", text_type=TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
    
    
    def test_generates_correct_nodes_from_two_images(self):
        nodelist = [
            TextNode(text="This is regular text", text_type=TextType.TEXT), 
            TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and it's great!", text_type=TextType.TEXT)
            ]
        
        transformed_nodelist = split_nodes_image(nodelist)
        
        expected_nodelist = [
            TextNode(text="This is regular text", text_type=TextType.TEXT), 
            TextNode(text="This is text with a ", text_type=TextType.TEXT), 
            TextNode(text="rick roll", text_type=TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="obi wan", text_type=TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(text=" and it's great!", text_type=TextType.TEXT)
            ]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
    

    def test_does_not_extract_link_markdown(self):
        nodelist = [
            TextNode(text="This is text with a link [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        
        transformed_nodelist = split_nodes_image(nodelist)
        
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_extracts_image_from_text_but_not_link_markdown(self):
        nodelist = [
            TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT), 
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        
        transformed_nodelist = split_nodes_image(nodelist)

        expected_nodelist = [ 
            TextNode(text="This is text with a ", text_type=TextType.TEXT), 
            TextNode(text="rick roll", text_type=TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
            TextNode(text=" and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT),
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
        
if __name__ == "__main__":
    unittest.main()