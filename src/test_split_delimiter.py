import unittest
from split_delimiter import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.Normal_Text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_Text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_Text),
                TextNode("bolded", TextType.Bold_Text),
                TextNode(" word", TextType.Normal_Text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.Normal_Text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_Text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_Text),
                TextNode("bolded", TextType.Bold_Text),
                TextNode(" word and ", TextType.Normal_Text),
                TextNode("another", TextType.Bold_Text),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.Normal_Text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_Text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_Text),
                TextNode("bolded word", TextType.Bold_Text),
                TextNode(" and ", TextType.Normal_Text),
                TextNode("another", TextType.Bold_Text),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.Normal_Text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.Italic_text)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Normal_Text),
                TextNode("italic", TextType.Italic_text),
                TextNode(" word", TextType.Normal_Text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.Normal_Text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_Text)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.Italic_text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.Bold_Text),
                TextNode(" and ", TextType.Normal_Text),
                TextNode("italic", TextType.Italic_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.Normal_Text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.Code_Text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_Text),
                TextNode("code block", TextType.Code_Text),
                TextNode(" word", TextType.Normal_Text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],matches)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.Normal_Text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Normal_Text),
                TextNode("image", TextType.Images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.Normal_Text),
                TextNode(
                    "second image", TextType.Images, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.Normal_Text,
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link",TextType.Normal_Text),
                TextNode("to boot dev",TextType.Links,"https://www.boot.dev"),
                TextNode("and",TextType.Normal_Text),
                TextNode("to youtube",TextType.Links,"https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )
if __name__ == "__main__":
    unittest.main()
