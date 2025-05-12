import re

def extract_markdown_links(text):
    matches = re.findall("(?<!\\!)\\[(.*?)\\]\\((.*?)\\)", text)
    return matches