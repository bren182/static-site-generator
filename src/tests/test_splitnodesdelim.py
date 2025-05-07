import unittest

from src.splitnodesdelim import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodesDelim(unittest.TestCase):

    def test_can_split_code_blocks(self):
        text_node = TextNode("Here's a `code` block!", TextType.NORMAL_TEXT)
        link_node = TextNode("Here is a link too!", TextType.LINKS, "https://google.com")
        new_node = split_nodes_delimiter([text_node, link_node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_node, [TextNode("Here's a ", TextType.NORMAL_TEXT), 
                                    TextNode("code", TextType.CODE_TEXT),
                                    TextNode(" block!", TextType.NORMAL_TEXT)])
    def test_raise_exception_on_unterminated_delimiter(self):
        bad_delim_text_node = TextNode("`Here is a very bad `code` block.", TextType.NORMAL_TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([bad_delim_text_node], "`",TextType.NORMAL_TEXT)
    
    def test_can_split_bold(self):
        bold_text_node = TextNode("Here's some **bold** text!", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([bold_text_node], "**",TextType.BOLD_TEXT)
        self.assertEqual(new_nodes,[
                             TextNode("Here's some ", TextType.NORMAL_TEXT),
                             TextNode("bold", TextType.BOLD_TEXT),
                             TextNode(" text!", TextType.NORMAL_TEXT)]
                         )

    def test_can_split_italics(self):
        italic_text_node = TextNode("Here is _italic_ text _here_", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([italic_text_node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes,[
            TextNode("Here is ", TextType.NORMAL_TEXT),
                             TextNode("italic", TextType.ITALIC_TEXT),
                             TextNode(" text ", TextType.NORMAL_TEXT),
                             TextNode("here", TextType.ITALIC_TEXT)])
    
    def test_can_split_nested(self):
        nested_text_node = TextNode("Here is **nested _stuff_**", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([nested_text_node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("Here is **nested ", TextType.NORMAL_TEXT),
            TextNode("stuff", TextType.ITALIC_TEXT),
            TextNode("**", TextType.NORMAL_TEXT)
        ])



