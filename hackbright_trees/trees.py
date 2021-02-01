from model import Node

if __name__ == '__main__':

    root = Node('Root', [])
    
    root.children.append(Node('Child_1', []))
    root.children.append(Node('Child_2', []))

    print(root.children)