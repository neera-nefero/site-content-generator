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

