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
    if len(old_nodes) == 0:
        return
    for node in old_nodes:
        img_tuple = extract_markdown_images(node.text)
        if len(img_tuple) == 0:
            return
        split_array = str.split(node.text, f'![{img_tuple[0][0]}]({img_tuple[0][1]})')
        # now we have an array, 0th element is before the split, then we add image and then after split
        # after split there may be more images 
        text_node_before = TextNode(split_array[0],TextType.NORMAL_TEXT)
        image_node = TextNode(img_tuple[0][0], TextType.IMAGES, img_tuple[0][1])
        text_after = split_nodes_image([TextNode(split_array[1],TextType.NORMAL_TEXT)])
        final_nodes.append(text_node_before)
        final_nodes.append(image_node)
        #print(f'before appending... what is text after {text_after}')
        if text_after is not None:
            final_nodes.extend(text_after)
    return final_nodes



def split_nodes_link(old_nodes):
    final_nodes = []
    if len(old_nodes) == 0:
        return
    for node in old_nodes:
        link_tuple = extract_markdown_links(node.text)
        if len(link_tuple) == 0:
            return
        split_array = str.split(node.text, f'[{link_tuple[0][0]}]({link_tuple[0][1]})')
        # now we have an array, 0th element is before the split, then we add link and then after split
        # after split there may be more links 
        text_node_before = TextNode(split_array[0],TextType.NORMAL_TEXT)
        link_node = TextNode(link_tuple[0][0], TextType.LINKS, link_tuple[0][1])
        text_after = split_nodes_link([TextNode(split_array[1],TextType.NORMAL_TEXT)])
        if text_node_before.text != '':
            final_nodes.append(text_node_before)
        final_nodes.append(link_node)
        #print(f'before appending... what is text after {text_after}')
        if text_after is not None:
            final_nodes.extend(text_after)
    return final_nodes