from enum import Enum
from src.markdown_to_blocks import markdown_to_blocks
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