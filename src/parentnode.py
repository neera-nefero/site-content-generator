from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, 
        tag: str,
        children: list["HTMLNode"], 
        props: dict[str, str]|None = None
    ) -> None:
        super().__init__(tag, None, children, props)    

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Children is required")
        html = ""
        for child in self.children:
            html += f"<{self.tag}{super().props_to_html()}>{child.to_html()}</{self.tag}>"
        return html

    def __eq__(self, other):
        return self.tag == other.tag and self.children == other.vachildrenlue and self.props == other.props    

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"




