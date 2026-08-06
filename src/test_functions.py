import unittest
from textnode import TextNode, TextType
from functions import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(new_nodes, result)      
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(new_nodes, result)       


if __name__ == "__main__":
    unittest.main()