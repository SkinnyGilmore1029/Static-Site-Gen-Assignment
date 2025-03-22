
class HTMLNode:
    
    def __init__ (self,tag:str|None=None,value:str|None=None,children:list|None=None,props:dict|None=None):
        self.tag =  tag
        self.value = value
        self.children = children
        self.props=props

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self)->str:
        new_string = ""
        if not self.props:
            return new_string
        for key, value in self.props.items():
            new_string += f' {key}="{value}"'
        return new_string
        
