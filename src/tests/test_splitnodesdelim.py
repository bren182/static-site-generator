import unittest

from src.splitnodesdelim import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_text_nodes
from src.textnode import TextNode, TextType

class TestSplitNodesDelim(unittest.TestCase):

    def test_can_split_code_blocks(self):
        text_node = TextNode("Here's a `code` block!", TextType.NORMAL_TEXT)
        link_node = TextNode("Here is a link too!", TextType.LINKS, "https://google.com")
        new_node = split_nodes_delimiter([text_node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_node, [TextNode("Here's a ", TextType.NORMAL_TEXT), 
                                    TextNode("code", TextType.CODE_TEXT),
                                    TextNode(" block!", TextType.NORMAL_TEXT)],
                                    TextNode("Here is a link too!", TextType.LINKS))
        
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
    
    def test_can_split_various(self):
        various_text_node = TextNode("Here is a _underlined_ part and a *bold part* in normal text", TextType.NORMAL_TEXT)
        new_nodes =  split_nodes_delimiter([various_text_node], "*", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
        
        self.assertEqual(new_nodes, [
            TextNode("Here is a ", TextType.NORMAL_TEXT),
            TextNode("underlined", TextType.ITALIC_TEXT),
            TextNode(" part and a ", TextType.NORMAL_TEXT),
            TextNode("bold part", TextType.BOLD_TEXT),
            TextNode(" in normal text", TextType.NORMAL_TEXT)
        ])

    
    def test_split_images_two(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_three(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and one last one for ![good measure](https://some.image.result)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and one last one for ", TextType.NORMAL_TEXT),
                TextNode("good measure", TextType.IMAGES, "https://some.image.result")
            ],
            new_nodes,
        )

    def test_split_three_stacked_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)![good measure](https://some.image.result)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("good measure", TextType.IMAGES, "https://some.image.result")
            ],
            new_nodes,
        )
    
    def test_images_with_text_at_end(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some text afterwards that should be accounted for!",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
                            TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text afterwards that should be accounted for!", TextType.NORMAL_TEXT)
        ])
    
    def test_images_with_broken_markdown(self):
        node = TextNode("Image with ![broken formatting](wow", TextType.NORMAL_TEXT)
        self.assertRaises(Exception,split_nodes_image([node]))
    
    def test_split_links_two(self):
        node = TextNode(
            "This is text with a link to [google](https://google.com) and another link [to youtube](https://youtube.com)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.NORMAL_TEXT),
                TextNode("google", TextType.LINKS, "https://google.com"),
                TextNode(" and another link ", TextType.NORMAL_TEXT),
                TextNode(
                    "to youtube", TextType.LINKS, "https://youtube.com"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_three(self):
        node = TextNode(
            "This is text with a link to [google](https://google.com) and another link [to youtube](https://youtube.com)[random link](https://some-random-place.com)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to ", TextType.NORMAL_TEXT),
                TextNode("google", TextType.LINKS, "https://google.com"),
                TextNode(" and another link ", TextType.NORMAL_TEXT),
                TextNode(
                    "to youtube", TextType.LINKS, "https://youtube.com"
                ),
                TextNode("random link",TextType.LINKS, "https://some-random-place.com")
            ],
            new_nodes,
        )
    def test_markdown_text_to_nodes(self):
        sample_text = "This is **text** with an _italic_ word and a `code block`"
        new_nodes = text_to_text_nodes(sample_text)
        self.assertEqual(new_nodes, [
            TextNode("This is ",TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT)
        ])


    def test_text_to_nodes(self):
        sample_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_text_nodes(sample_text)
        self.maxDiff = None
        self.assertEqual(new_nodes, [
                            TextNode("This is ", TextType.NORMAL_TEXT),
                            TextNode("text", TextType.BOLD_TEXT),
                            TextNode(" with an ", TextType.NORMAL_TEXT),
                            TextNode("italic", TextType.ITALIC_TEXT),
                            TextNode(" word and a ", TextType.NORMAL_TEXT),
                            TextNode("code block", TextType.CODE_TEXT),
                            TextNode(" and an ", TextType.NORMAL_TEXT),
                            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.NORMAL_TEXT),
                            TextNode("link", TextType.LINKS, "https://boot.dev"),
                        ])
    
    def test_text_to_nodes_mixup(self):
        sample_text = "_Lets start_ with some [random link](https://google.com) to `coding`"
        new_nodes = text_to_text_nodes(sample_text)
        self.assertEqual(new_nodes, [
            TextNode("Lets start", TextType.ITALIC_TEXT),
            TextNode(" with some ", TextType.NORMAL_TEXT),
            TextNode("random link", TextType.LINKS, url="https://google.com"),
            TextNode(" to ", TextType.NORMAL_TEXT),
            TextNode("coding", TextType.CODE_TEXT)
        ])




