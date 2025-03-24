import unittest

from node_transformations import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):        
    def test_raises_when_list_of_nodes_not_given(self):
        node = TextNode(text="This is plain text", text_type=TextType.TEXT)
        with self.assertRaises(TypeError):
            split_nodes_link(node)
        

    def test_returns_list_unchanged_if_no_Text_TextType(self):
        nodelist = [TextNode(text="This is bold text", text_type=TextType.BOLD), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        transformed_nodelist = split_nodes_link(nodelist)
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_returns_list_unchanged_Text_has_no_links(self):
        nodelist = [TextNode(text="This is regular text", text_type=TextType.TEXT), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        transformed_nodelist = split_nodes_link(nodelist)
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_generates_correct_nodes_from_single_link(self):
        nodelist = [TextNode(text="This is text with a link [to boot dev](https://www.boot.dev)", text_type=TextType.TEXT), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        
        transformed_nodelist = split_nodes_link(nodelist)
        
        expected_nodelist = [TextNode(text="This is text with a link ", text_type=TextType.TEXT), TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
    
    
    def test_generates_correct_nodes_from_two_links(self):
        nodelist = [TextNode(text="This is regular text", text_type=TextType.TEXT), TextNode(text="This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and it's great!", text_type=TextType.TEXT)]
        
        transformed_nodelist = split_nodes_link(nodelist)
        
        expected_nodelist = [
            TextNode(text="This is regular text", text_type=TextType.TEXT), 
            TextNode(text="This is text with a link ", text_type=TextType.TEXT), 
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=" and it's great!", text_type=TextType.TEXT)
            ]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
    

    def test_does_not_extract_image_markdown(self):
        nodelist = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", text_type=TextType.TEXT), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        
        transformed_nodelist = split_nodes_link(nodelist)
        
        self.assertSequenceEqual(transformed_nodelist, nodelist, list)
    
    def test_extracts_link_from_text_but_not_image_markdown(self):
        nodelist = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT), TextNode(text="This is italic text", text_type=TextType.ITALIC)]
        
        transformed_nodelist = split_nodes_link(nodelist)

        expected_nodelist = [ 
            TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ", text_type=TextType.TEXT),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text="This is italic text", text_type=TextType.ITALIC)
            ]
        self.assertSequenceEqual(transformed_nodelist, expected_nodelist, list)
        
if __name__ == "__main__":
    unittest.main()