class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children= children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        final_props = ""
        for key in self.props:  
            final_props += key + "=" + "\"" + self.props[key] + "\" "
        return final_props.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


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

