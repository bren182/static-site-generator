import unittest
from src.markdown_blocks import BlockTypes, block_to_block_type
class MarkdownBlockTests(unittest.TestCase):
    def test_can_identify_quote_block(self):
        md = """> Quote here
> And here
> Valid quote"""
        self.assertEqual(block_to_block_type(md), BlockTypes.QUOTE)
    
    def test_can_identify_unordered_list_block(self):
        md = """- here
- And here
- Valid quote"""
        self.assertEqual(block_to_block_type(md), BlockTypes.UNORDERED_LIST)

    def test_can_identify_ordered_list_block(self):
        md = """1. here
2. And here
3. Valid quote"""
        self.assertEqual(block_to_block_type(md), BlockTypes.ORDERED_LIST)

    def test_can_identify_code_block(self):
        md = """```here
2. And here
3. Valid quote```"""
        self.assertEqual(block_to_block_type(md), BlockTypes.CODE)

    def test_can_identify_code_block(self):
        md = """here US a paragraph
3. Valid quote```"""
        self.assertEqual(block_to_block_type(md), BlockTypes.PARAGRAPH)

