import unittest
from src.htmlnode import LeafNode


class LeafNodeTest(unittest.TestCase):
    def test_leaf_node_to_html(self):
        node = LeafNode("p","Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")
    
    def test_assert_equal(self):
        node1 = LeafNode("p","Hello world")
        node2 = LeafNode("p", "Hello world")
        self.assertEqual(repr(node1), repr(node2))

    def test_assert_not_equal(self):
        node1 = LeafNode("p", "Whahoo!")
        node2 = LeafNode("p", "Ha")
        self.assertNotEqual(node1, node2)

    def test_empty_base_node(self):
        empty_node = LeafNode(None, "Whahoo!")
        self.assertEqual(empty_node.to_html(), "Whahoo!")
    
    def test_link_node(self):
        link_node = LeafNode("a", "Link to thing!", {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(link_node.to_html(), "<a href=\"https://google.com\" target=\"_blank\">Link to thing!</a>")


