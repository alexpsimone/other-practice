from binarytree import tree
import random

def make_some_negative(root):
    if root is not None:
        if random.random() > .5:
            root.val = -root.val
        make_some_negative(root.left)
        make_some_negative(root.right)

def find_highest_sum(root):
    
    if root is None:
        return 0
    
    left_sum = find_highest_sum(root.left) + root.val
    right_sum = find_highest_sum(root.right) + root.val

    if left_sum > right_sum:
        return left_sum
    else:
        return right_sum


if __name__ == '__main__':
    t = tree(2)
    print(t)

    make_some_negative(t)

    print(t)

    print(find_highest_sum(t))