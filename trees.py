from model import Node

if __name__ == '__main__':

    root = Node('Dumbledore', [])
    
    root.children.append(Node('Snape', []))
    root.children.append(Node('Flitwick', []))

    print(root.children)