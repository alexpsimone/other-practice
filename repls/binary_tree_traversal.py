from binarytree import tree

# preorder, inorder
# tree traversal
# I give you a binary tree, and you have to output the values at all the nodes in a specified order (which I will describe)

#     2
#    / \
#   4   6
#  /     \
# 0       1


#     6__
#    /   \
#   2     0
#  /     / \
# 3     1   5

# 6, 2, 3, 0, 1, 5 -> preorder traversal of this tree
# 3, 2, 6, 1, 0, 5 -> inorder traversal of the tree
# I want to process the node n and then all of its left children before any of its right children


#       ________5
#      /         \
#     7___        6___
#    /    \           \
#   1     _9          _11
#  /     /  \        /
# 0     10   12     13


# 5, 7, 1, 0, 9, 10, 12, 6, 11, 13
# 0, 1, 7, 10, 9, 12, 5, 6, 13, 11 
# In order traversal is going be process left child first, then process the node I am at, then process the right children

# class Node(object):

#     def __init__(self, value, left=None, right=None):
#         self.val = value    # The node value
#         self.left = left    # Left child
#         self.right = right  # Right child


#   1
#  / \
# 2   0


def preorder(root):

    # if root isn't None
    if root != None:
        # right away, i should emit root
        print(root.val)
        # recurse on the left subtree
        preorder(root.left)
        # recurse on the right subtree 
        preorder(root.right)

def inorder(root):
    
    # if root isn't none
    if root != None:
        # recurse on left child
        for n in inorder(root.left):
            yield n
        # print node I'm at
        yield root
        # recurse on right child
        for n in inorder(root.right):
            yield n
def postorder(root):

    # if root isn't none:
    if root != None:
        # recurse on left child
        postorder(root.left)
        # recurse on right child
        postorder(root.right)
        # print current node
        print(root.val)


def my_range_generator(n):
    i = 0
    while i < n:
        # emit i
        # if i print i, it is printed out but i cant access it
        # if i return i, the function stops
        yield i
        i += 1


if __name__ == '__main__':
    t = tree(3)
    print(t)