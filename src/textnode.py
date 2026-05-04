from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # 1. If old_node is not a TEXT type, append it as-is and continue
        if old_node is not text_type:
            new_nodes.append(old_node)
        elif old_node is text_type:
            parts = old_node.split({delimiter})
            if not len(parts) % 3:
                raise Exception("Unmatched delimitter")
        # 2. Otherwise, split old_node.text using the delimiter
        #    e.g. parts = old_node.text.split(delimiter)
        
        # 3. If the number of parts is even, there's an unmatched delimiter
        #    -> raise an exception
        
        # 4. Loop through the parts:
        #    - even-indexed parts are plain TEXT
        #    - odd-indexed parts are the special text_type
        #    - skip empty strings if you like
        #    - append each as a TextNode to a temporary list
        
        # 5. extend new_nodes with that temporary list
        pass
    return new_nodes