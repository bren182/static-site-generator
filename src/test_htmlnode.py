import unittest
from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def testPropsToHtml(self):
        htmlnode = HTMLNode("a", "a link!", None, {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(htmlnode.props_to_html(), f"href=\"https://google.com\" target=\"_blank\"")
    
    def testToHtmlNotImplemented(self):
        htmlnode = HTMLNode("p", "a paragraph!", None)
        with self.assertRaises(NotImplementedError):
            htmlnode.to_html()

    def assertHtmlNodesEqual(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def assertHtmlNodesNotEqual(self):
        node1 = HTMLNode("p")
        node2 = HTMLNode("a")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()

