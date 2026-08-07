import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_list.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown syntax")

        chain_count = 1
        for chain in node.text.split(delimiter):
            if chain_count % 2 != 0:
                new_list.append(TextNode(chain, TextType.TEXT))
            else:
                new_list.append(TextNode(chain, text_type))
            chain_count += 1

    return new_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if links == "":
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        text_to_split = node.text
        for alt, src in links:
            before, remaining = text_to_split.split(f"![{alt}]({src})", 1)
            text_to_split = remaining
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, src))
    return new_nodes
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == "":
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        text_to_split = node.text
        for label, url in links:
            before, remaining = text_to_split.split(f"[{label}]({url})", 1)
            text_to_split = remaining
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(label, TextType.LINK, url))
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)