
class HTMLNode:
    
    def __init__ (self,tag:str|None=None,value:str|None=None,children:list|None=None,props:dict|None=None):
        self.tag =  tag
        self.value = value
        self.children = children
        self.props=props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self)->str:
        new_string = ""
        if not self.props:
            return new_string
        for key, value in self.props.items():
            new_string += f' {key}="{value}"'
        return new_string
        
class LeafNode(HTMLNode):
    def __init__(self,tag:str,value:str,props:dict|None = None):
        super().__init__(tag,value,props=props)
        
    def to_html(self)->str:
        attrs = ''
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        if self.props != None:
            for key, value in self.props.items():
                attrs += f' {key}="{value}"'
                
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"