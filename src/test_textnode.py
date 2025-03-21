import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node",TextType.Bold_Text)
        node2 = TextNode("This is a text node",TextType.Bold_Text)
        self.assertEqual(node,node2)
        
    def test_link(self):
        node = TextNode("This is a link node",TextType.Links)
        node2 = TextNode("This is a link node",TextType.Links)
        self.assertEqual(node,node2)
        
    def test_url(self):
        node = TextNode("This has a url",TextType.Links,"https://www.boot.dev")
        node2 = TextNode("This has no url",TextType.Links)
        self.assertNotEqual(node,node2)
        
        
if __name__ =="__main__":
    unittest.main()