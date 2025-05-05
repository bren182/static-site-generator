from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        # print(f'Parent node initializing: self,tag,value,children,props {self} , {tag} , {value} , {children} , {props}')
        super().__init__(tag,None, children, props)

    def to_html(self):
        if self.tag  == None:
            raise ValueError("No tag value provided")
        if self.children == None:
            raise ValueError("No children value provided")
        # recursion 
        # base case is children is empty, so return current self tag and value, 
        if self.children == []:
            # don't have to recur further, return the child 
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            final_html = []
            for child in self.children:
                inner_children_html = child.to_html()
                final_html.append(inner_children_html)
            return f"<{self.tag}>{"".join(final_html)}</{self.tag}>"

