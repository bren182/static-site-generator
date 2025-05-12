def markdown_to_blocks(markdown):
    final_blocks = []
    split_lines = str.split(markdown, "\n\n")
    for line in split_lines:
        # if we encounter a list element, we replace any new lines so it falls into a single line
        if '-' in line:
            line.replace('\n', '')
        final_blocks.append(line.strip())
    return final_blocks
