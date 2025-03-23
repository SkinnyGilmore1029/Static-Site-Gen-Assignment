from textnode import TextType,TextNode


def split_nodes_delimiter(old_nodes:list[object], delimiter, text_type)->list[object]: #just so i remember what i am working with and what it wants returned Object is a Node
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.Normal_Text:
            new_nodes.append(node)
        else:
            if delimiter in node.text:
                first = node.text.find(delimiter)
                last = node.text.find(delimiter,first + len(delimiter))
                if last == -1:
                    raise Exception("Invalid markdown: missing closing delimiter")
                before_text = node.text[:first]
                special_text = node.text[first + len(delimiter):last]
                after_text = node.text[last + len(delimiter):]
                if before_text:
                    new_nodes.append(TextNode(before_text, TextType.Normal_Text))
                new_nodes.append(TextNode(special_text, text_type))
                if after_text:
                    new_nodes.append(TextNode(after_text, TextType.Normal_Text))
            else:
                new_nodes.append(node)
    return new_nodes