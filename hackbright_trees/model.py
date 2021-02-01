# Node Class
class Node():
    """A node object in a tree."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


    def __repr__(self):
        """User-friendly representation"""

        return f'<Node {self.data}>'


    def dfs(self, data):
        """Return node object with the given data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current
            
            to_visit.extend(current.children)
    

    def recursive_dfs(self, data):
        """Search for Node object with given data, recursively."""

        pass