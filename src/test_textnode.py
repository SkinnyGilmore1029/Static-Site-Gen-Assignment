import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.Normal_Text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is bold", TextType.Bold_Text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_links(self):
        node = TextNode("Click here", TextType.Links, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_images(self):
        node = TextNode("Alt text", TextType.Images, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Alt text"})
        
if __name__ =="__main__":
    unittest.main()