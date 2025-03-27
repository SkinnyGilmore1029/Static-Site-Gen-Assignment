from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block) -> BlockType:
    my_lines = block.split('\n')
    
    # Check for headings
    hash_count = 0
    for c in block:
        if c == "#":
            hash_count += 1
        else:
            break
    
    if 1 <= hash_count <= 6 and len(block) > hash_count and block[hash_count] == " ":
        return BlockType.HEADING
    
    # Check for code blocks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote blocks
    if all(line.startswith(">") for line in my_lines):
        return BlockType.QUOTE
    
    # Check for unordered lists
    if all(line.startswith("- ") for line in my_lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered lists
    expected_number = 1
    is_ordered_list = True
    
    for line in my_lines:
        if not line.startswith(str(expected_number) + ". "):
            is_ordered_list = False
            break
        expected_number += 1
        
    if is_ordered_list and expected_number:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
