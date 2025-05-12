from src.textnode import TextNode, TextType
from src.extract_markdown_images import extract_markdown_images
from src.extract_markdown_links import extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for node in old_nodes:
        # we loop through each nodes
        # if its not a text node, just add it to final nodes
        if node.text_type != TextType.NORMAL_TEXT:
            final_nodes.append(node)
        # loop through the text in the node
        else:
            split_delim = str.split(node.text, delimiter)
            if len(split_delim) % 2 == 0:
                raise Exception("Invalid markdown syntax. Unable to find a closing delimiter.")
            for i in range(0, len(split_delim)):
                if i % 2 == 0:
                    if split_delim[i] != '':
                        final_nodes.append(TextNode(split_delim[i], TextType.NORMAL_TEXT))
                else:
                    final_nodes.append(TextNode(split_delim[i], text_type))
    return final_nodes

def split_nodes_image(old_nodes):
    final_nodes = []
    for node in old_nodes:
        current_text = node.text
        img_split = extract_markdown_images(current_text)
        if len(img_split) == 0:
            if node.text != '':
                final_nodes.append(node)
                continue
        for img in img_split:
            str_split = str.split(current_text, f'![{img[0]}]({img[1]})')
            text_node_before = TextNode(str_split[0],TextType.NORMAL_TEXT)
            img_node = TextNode(img[0], TextType.IMAGES, img[1])
            if text_node_before.text != '':
                final_nodes.append(text_node_before)
            final_nodes.append(img_node)
            current_text = str_split[1]
        if current_text != '':
            after_image_text = TextNode(current_text, TextType.NORMAL_TEXT)
            final_nodes.append(after_image_text)
    return final_nodes

def split_nodes_link(old_nodes):
    final_nodes = []
    for node in old_nodes:
        current_text = node.text
        link_split = extract_markdown_links(current_text)
        if len(link_split) == 0:
            if node.text != '':
                final_nodes.append(node)
                continue
        for link in link_split:
            str_split = str.split(current_text, f'[{link[0]}]({link[1]})')
            text_node_before = TextNode(str_split[0],TextType.NORMAL_TEXT)
            link_node = TextNode(link[0], TextType.LINKS, link[1])
            if text_node_before.text != '':
                final_nodes.append(text_node_before)
            final_nodes.append(link_node)
            current_text = str_split[1]
        if current_text != '':
            after_link_text = TextNode(current_text, TextType.NORMAL_TEXT)
            final_nodes.append(after_link_text)
    return final_nodes

def text_to_text_nodes(text):
    final_nodes = split_nodes_delimiter([TextNode(text,TextType.NORMAL_TEXT)],"**",TextType.BOLD_TEXT)
    final_nodes = split_nodes_delimiter(final_nodes,"_",TextType.ITALIC_TEXT)
    final_nodes = split_nodes_delimiter(final_nodes,"`",TextType.CODE_TEXT)
    final_nodes = split_nodes_image(final_nodes)
    #print(f'final nodes after image split! {final_nodes}')
    final_nodes = split_nodes_link(final_nodes)
    return final_nodes


