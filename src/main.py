from htmlnode import HTMLNode

def main():
    htmlnode = HTMLNode("<p>", None, None, {"href":"http://example.com"})
    print(htmlnode)

main()