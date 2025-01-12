from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str|None, children:list["HTMLNode"]|None, props:dict[str,str]|None=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        else:
            return f"<{self.tag}{self.props_to_html() if self.props else ''}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
        
    def __repr__(self):
        return f"""ParentNode({f"tag='{self.tag}'" if self.tag != None else f'tag={self.tag}'}, children={self.children}, props={self.props})"""