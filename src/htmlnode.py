class HTMLNode():
    def __init__(
        self, 
        tag: str|None = None, 
        value: str|None = None, 
        children: list["HTMLNode"]|None = None, 
        props: dict[str, str]|None = None
    ) -> None:        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props        

    def props_to_html(self) -> str:
        if self.props is not None:
            result = ""
            for prop in self.props:
                result += f' {prop}="{self.props[prop]}"'
            return result
        return ""

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")