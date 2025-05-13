from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = "parapgraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST= "ordered_list"

def block_to_block_type(markdown):
    isquote = False
    isheading = False
    iscode = False
    isuolist = False
    isolist = False
    counter = 1
    lines = markdown_to_blocks(markdown)
    for line in lines:
        if str.startswith(line, ">"):
            isquote = True
        else:
            isquote = False
        if str.startswith(line,"- "):
            isuolist = True
        else:
            isuolist = False
        if str.startswith(line, f'{counter}. '):
            isolist = True
        else:
            isolist = False
        if str.startswith(line, "```") and str.endswith(line,"```"):
            return BlockTypes.CODE
        counter += 1
    if isquote:
        return BlockTypes.QUOTE
    if isuolist:
        return BlockTypes.UNORDERED_LIST
    if isolist:
        return BlockTypes.ORDERED_LIST
    return BlockTypes.PARAGRAPH

def markdown_to_blocks(markdown):
    final_blocks = []
    split_lines = str.split(markdown, "\n\n")
    for line in split_lines:
        # if we encounter a list element, we replace any new lines so it falls into a single line
        if '-' in line:
            line.replace('\n', '')
        final_blocks.append(line.strip())
    return final_blocks

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown=markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        html_from_block = create_html_from_block(block, block_type)
        pass

def create_html_from_block(block, block_type):
    pass