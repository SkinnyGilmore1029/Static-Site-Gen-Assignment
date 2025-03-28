from markdown_blocks import markdown_to_blocks,block_to_block_type
from htmlnode import HTMLNode
from split_delimiter import split_nodes_delimiter
from textnode import TextType,TextNode,text_node_to_html_node

def text_to_children(text):
    # Start with a single TextNode containing the entire text
    nodes = [TextNode(text, TextType.Normal_Text)]
    
    # Process each inline delimiter
    nodes = split_nodes_delimiter(nodes, "**", TextType.Bold)
    nodes = split_nodes_delimiter(nodes, "*", TextType.Italic)
    nodes = split_nodes_delimiter(nodes, "_", TextType.Italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.Code)
    
    # Convert TextNodes to HTMLNodes
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    
    return html_nodes

def process_paragraph(block):
    paragraph_text = block.strip()
    return HTMLNode("p",None,None,text_node_to_html_node(paragraph_text))

def process_heading(block):
    count = 0
    for char in block:
        if char == "#":
            count +=1
    heading_text = block[count:].strip()
    return HTMLNode(f"h{count}",None,None,text_to_children(heading_text))

def process_code(block):
    # Remove triple backticks and extract code content
    lines = block.split('\n')
    # Remove the first and last line (which contain ```)
    code_lines = lines[1:-1] if len(lines) > 2 else []
    
    # Join the code lines back together
    code_text = '\n'.join(code_lines)
    
    # Create a TextNode with the code content
    code_text_node = TextNode(code_text, TextType.Normal_Text)
    
    # Convert to HTML node
    code_html_node = text_node_to_html_node(code_text_node)
    
    # Create a node with the code node as its child
    return  HTMLNode("pre", None, None, [HTMLNode("code", None, None, [code_html_node])])
    
def process_quotes(block)->bool:
    block_lines = block.split('\n')
    split_lines = []
    for line in block_lines:
        if line.startswith(">"):
            new_line = line[1:].strip()
            split_lines.append(new_line)
        quote_text = "\n".join(new_line)
    return HTMLNode("blockquote",None,None,text_to_children(quote_text))

def process_unordered_list(block):
    block_lines = block.split('\n')
    new_text = []
    for line in block_lines:
        if line.startswith( "- "):
            new_line = line[2:].strip()
            new_text.append(HTMLNode("li",None,None,text_to_children(new_line)))
    return HTMLNode("ul",None,None,new_text)
            
def process_ordered_list(block):
    block_lines = block.split("\n")
    list_items = []
    
    for line in block_lines:
        # Check if line matches ordered list pattern
        import re
        if re.match(r'^\d+\.\s', line):
            # Find where the actual content starts (after the number, period, and space)
            content_start = line.find('. ') + 2
            if content_start >= 2:  # Make sure we found '. '
                item_text = line[content_start:].strip()
                # Create an li node for this item
                list_items.append(HTMLNode("li", None, None, text_to_children(item_text)))
    
    # Return an ol node with all the li nodes as children
    return HTMLNode("ol", None, None, list_items)
    
def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in md_blocks:
        block_types = block_to_block_type(block)
        match block_types:
            case "paragraph":
                block_nodes.append(process_paragraph(block))
            case "heading":
                block_nodes.append(process_heading(block))
            case "code":
                block_nodes.append(process_code(block))
            case "quote":
                block_nodes.append(process_quotes(block))
            case "unordered list":
                block_nodes.append(process_unordered_list(block))
            case "ordered list":
                block_nodes.append(process_ordered_list(block))
    parent_node =HTMLNode("div",None,None,block_nodes)
    return parent_node
