from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, 
        tag: str|None, 
        value: str|None,
        props: dict[str, str]|None = None
    ) -> None:
        super().__init__(tag, value, None, props)    

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props    

    def __repr__(self) -> str:
        return f"LEAFNode({self.tag}, {self.value}, {self.props})"




