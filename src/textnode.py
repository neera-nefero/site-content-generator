from enum import Enum


class TextType(Enum):
    TEXT_TYPE = "text"
    BOLD_TYPE = "bold"
    ITALIC_TYPE = "italic"
    CODE_TYPE = "code"
    LINK_TYPE = "link"
    IMAGE_TYPE = "image"

class TextNode():
    def __init__(self, text: str, type: TextType, url: str | None = None) -> None:
        self.text = text
        self.type = type
        self.url = url
    def __eq__(self, other):
        return self.text == other.text and self.type == other.type and self.url == other.url
    def __repr__(self):
        return f"{self.text}, {self.type.value}, {self.url}"