import unittest
from src.extract_markdown_links import extract_markdown_links
class TestExtractMarkdownLink(unittest.TestCase):

    def test_can_return_link_content(self):
        text = "This is text with a link [to google](https://google.com) and [to youtube](https://youtube.com)"
        self.assertEqual(extract_markdown_links(text), [("to google", "https://google.com"), ("to youtube", "https://youtube.com")])