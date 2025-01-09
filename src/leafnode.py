from multiprocessing import Value
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value:str, tag:str|None, props:dict[str,str]|None=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"""LeafNode({f"tag='{self.tag}'" if self.tag != None else f'tag={self.tag}'}, value='{self.value}', props={self.props})"""