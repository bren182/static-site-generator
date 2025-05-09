import re
def extract_markdown_images(text):
    matches = re.findall("\\!\\[(.*?)\\]\\((.*?)\\)", text)
    return matches

