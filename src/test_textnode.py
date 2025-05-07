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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINKS, "https://google.com")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")

    def test_img(self):
        node = TextNode("This is an image node", TextType.IMAGES,"https://giphyimage.com")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt"], "This is an image node")
        self.assertEqual(html_node.props["src"], "https://giphyimage.com")
    
    def test_codeblock(self):
        node = TextNode("This is code", TextType.CODE_TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
    
    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
