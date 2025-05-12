import unittest
from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
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

    def test_markdown_to_blocks_various(self):
        md = """
I have an _underline_ here

- Here is a 
- big list
- with a whole lotta

- And then another list
- with more stuff
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "I have an _underline_ here",
            "- Here is a \n- big list\n- with a whole lotta",
            "- And then another list\n- with more stuff"
        ])