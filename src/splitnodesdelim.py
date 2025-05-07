from src.textnode import TextNode, TextType

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