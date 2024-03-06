import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
      node = HTMLNode(
            "div",
            "Hello world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        if attributes is not None:
            raise ValueError("LeafNode cannot have children")
        super().__init__(tag, value, {})
    
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        else:
            attribute_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
            return f"<{self.tag} {attribute_str}>{self.value}</{self.tag}>"

