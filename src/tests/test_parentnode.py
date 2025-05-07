import unittest
from src.htmlnode import ParentNode, LeafNode

class ParentNodeTest(unittest.TestCase):
    def test_can_construct(self):
        myparent = ParentNode("h1", "Heading1",None)
        self.assertEqual(type(myparent), ParentNode)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")  
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
    
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )