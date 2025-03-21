from enum import Enum

class TextType(Enum):
    Normal_Text = "Normal text"
    Bold_Text = "**Bold text**"
    Italic_text = "_Italic text_"
    Code_Text = "`Code text`"
    Links = "Link"
    Images = "Image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        return (self.text_type.value == other.text_type.value and
            self.text ==  other.text and
            self.url ==  other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"