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
    

    def bfs(self, data):
        """Return node object with the given data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current
        
        to_visit.extend(current.children)


    def recursive_dfs(self, data):
        """Search for Node object with given data, recursively."""

        pass
    
    def recursive_bfs(self, data):
        """Search for Node object with given data, recursively."""

        pass


# Tree Class
class Tree():
    """A tree object."""

    def __init__(self, root):
        self.root = root
    
    def __repr__(self):
        return f'<Tree root={self.root}>'
    
    def dfs_tree(self, data):
        """Return node object with the given data."""

        return self.root.dfs(data)
    
    def bfs_tree(self, data):
        """Return node object with the given data."""

        return self.root.bfs(data)