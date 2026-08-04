from textnode import TextType
from textnode import TextNode

def main():
    text = TextNode("This is some anchor text", TextType("link"), "https://www.boot.dev")
    print(f"TextNode({text})")

main()