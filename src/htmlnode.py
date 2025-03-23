
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
    
class ParentNode(HTMLNode):
    def __init__(self,tag:str,children:list,props:dict|None = None):
        super().__init__(tag,children=children,props=props)
    
    def to_html(self):
        if not self.tag: # check to see if tag is there..also helps break recursion
            raise ValueError("tag is not correct")
        if self.children == []: # checks to make sure its not an empty list... also helps break recursion
            raise ValueError("cannot be an empty list")
        results = '' #starting point for the string
        for child in self.children: # loops thro self.children and adds to_html to results
            results += child.to_html()
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{results}</{self.tag}>" # returns results 
