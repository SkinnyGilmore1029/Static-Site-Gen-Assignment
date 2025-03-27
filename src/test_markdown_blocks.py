import unittest
from markdown_blocks import markdown_to_blocks,block_to_block_type,BlockType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlocktoBlock(unittest.TestCase):
    def test_heading_block(self):
        block = "### I am supposed to be header."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
        
    def test_paragraph_block(self):
        block = "This is a normal paragraph with no special formatting."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('Hello World')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote_block(self):
        block = ">This is a quote\n>This is also part of the quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result,BlockType.ORDERED_LIST)
        
    def test_mixed_list_block(self):
        block = "1. Item 1\n- Item 2\n- Item 3"
        result = block_to_block_type(block)
        # This should be a paragraph because it doesn't match the pattern for ordered lists
        self.assertEqual(result, BlockType.PARAGRAPH)
if __name__ == "__main__":
    unittest.main()
