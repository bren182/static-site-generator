from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        tag_props = super().props_to_html()
        if tag_props == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag} {super().props_to_html().strip()}>{self.value}</{self.tag}>"


