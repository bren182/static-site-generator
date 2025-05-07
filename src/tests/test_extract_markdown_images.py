import unittest
from src.extract_markdown_images import extract_markdown_images
class TestExtractMarkdownImages(unittest.TestCase):

    def test_can_extract_image_markdown(self):
        result = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(result,[('rick roll','https://i.imgur.com/aKaOqIh.gif'), ('obi wan','https://i.imgur.com/fJRm4Vk.jpeg')])
