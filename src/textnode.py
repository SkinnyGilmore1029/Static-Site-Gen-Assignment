from enum import Enum
from htmlnode import LeafNode

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
    
def text_node_to_html_node(text_node:object):
    if text_node.text_type == TextType.Normal_Text:
        return LeafNode(None,text_node.text)
    elif text_node.text_type == TextType.Bold_Text:
        return LeafNode("b",text_node.text)
    elif text_node.text_type == TextType.Italic_text:
        return LeafNode("i",text_node.text)
    elif text_node.text_type == TextType.Code_Text:
        return LeafNode("code",text_node.text)
    elif text_node.text_type == TextType.Links:
        return LeafNode("a",text_node.text,{"href" : text_node.url})
    elif text_node.text_type == TextType.Images:
        return LeafNode("img","",{"src":text_node.url,
                                    "alt" :text_node.text})
    else:
        raise Exception("Unknown Type")