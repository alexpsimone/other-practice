from binarytree import tree
import random

def make_some_negative(root):
    if root is not None:
        if random.random() > .5:
            root.val = -root.val
        make_some_negative(root.left)
        make_some_negative(root.right)

#          ____5_______
#         /            \
#       _2         _____-9___
#      /  \       /          \
#    _-4   7     -6_         _12
#   /       \       \       /   \
# -11        0      -10    -8    14



#    _-4    
#   /      
# -11     

def find_min_sum_tree(root):

    # { node: find_sum(node)}
    sums_dict = {}

    def find_sum(root):
        
        if root is None:
            return 0
    
        if root in sums_dict:
            return sums_dict[root]

        sums_dict[root] = find_sum(root.left) + root.val + find_sum(root.right)
        return sums_dict[root]

    find_sum(root)
    # initialize a min_sum at None
    # traverse the tree, node by node
    # call find_sum on each node

    min_sum = None
    min_sum_node = None

    for dict_key in sums_dict:
        if min_sum is None:
            min_sum = sums_dict[dict_key]
            min_sum_node = dict_key
            
        elif min_sum > sums_dict[dict_key]:
            min_sum = sums_dict[dict_key]
            min_sum_node = dict_key
    
    # return min_sum_node
    # sorted(lst, key)
    return min(sums_dict.keys(), key=lambda x: sums_dict[x])
    # traverse sums_dict in one sick line to find the node with the smalled sum


def find_min_sum_2(root):

    # if root is not none
    # calculate find_min_sum_2(root.left)
    # calculate find_min_sum_2(root.right)

    if root is None:
        return 0, None, None

    left_tree_sum, left_min_seen_node, left_min_seen_sum = find_min_sum_2(root.left)
    right_tree_sum, right_min_seen_node, right_min_seen_sum = find_min_sum_2(root.right)
    
    root_sum = left_tree_sum + root.val + right_tree_sum
    
    if left_min_seen_node is None:
        left_min_seen_node = root
        left_min_seen_sum = root_sum
    
    if right_min_seen_node is None:
        right_min_seen_node = root
        right_min_seen_sum = root_sum

    if root_sum <= left_min_seen_sum and root_sum <= right_min_seen_sum:
        root_min_seen_node = root
        root_min_seen_sum = root_sum
    
    if right_min_seen_sum <= left_min_seen_sum and right_min_seen_sum <= root_sum:
        root_min_seen_node = right_min_seen_node
        root_min_seen_sum = right_min_seen_sum

    if left_min_seen_sum <= right_min_seen_sum and left_min_seen_sum <= root_sum:
        root_min_seen_node = left_min_seen_node
        root_min_seen_sum = left_min_seen_sum
    

    return root_sum, root_min_seen_node, root_min_seen_sum



# class Node(object):
    #
    # def __init__(self, value, left=None, right=None):
    #     self.val = value    # The node value
    #     self.left = left    # Left child
    #     self.right = right  # Right child


if __name__ == '__main__':
    t = tree(4)
    print(t)

    make_some_negative(t)

    print(t)

    print(find_min_sum_tree(t).val)

    root_sum, root_min_seen_node, root_min_seen_sum = find_min_sum_2(t)
    print(root_min_seen_node.val)