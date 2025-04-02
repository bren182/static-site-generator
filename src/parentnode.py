from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,value,children,props=None):
        print(f'Parent node initializing: self,tag,value,children,props {self} , {tag} , {value} , {children} , {props}')
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag  == None:
            raise ValueError("No tag value provided")
        if self.children == None:
            raise ValueError("No children value provided")



