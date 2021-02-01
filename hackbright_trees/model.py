# Node Class
class Node():
    """A node object in a tree."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def __repr__(self):
        """User-friendly representation"""

        return f'<Node {self.data}>'
