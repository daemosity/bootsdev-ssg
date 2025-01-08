class HTMLNode:
    def __init__(self, tag:str|None=None, value:str|None=None, children:list["HTMLNode"]|None=None, props:dict[str,str]|None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"