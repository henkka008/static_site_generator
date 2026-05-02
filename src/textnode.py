from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_url, url=None):
        self.text = text
        self.text_url = text_url
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_url == other.text_url and self.url == other.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_url}, {self.url})"
    


