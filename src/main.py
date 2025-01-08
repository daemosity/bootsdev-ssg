from textnode import TextNode, TextType

def main():
    textnode = TextNode("This is a text node", TextType.Bold, "https://www.boot.dev")
    print(textnode)

main()