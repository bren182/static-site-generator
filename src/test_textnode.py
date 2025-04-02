import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("Hi I am different than below me!", TextType.BOLD_TEXT)
        node2 = TextNode("I am different than above me!", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

    def test_none_url(self):
        node_none_url = TextNode("No url!", TextType.BOLD_TEXT)
        self.assertEqual(node_none_url.url, None)

if __name__ == "__main__":
    unittest.main()
