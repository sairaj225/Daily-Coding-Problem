
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Tree

"""
    0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.left.left = Node(1)
a.right.left.right = Node(1)
a.right.right = Node(0)


def is_unival(root):
    return unival_helper(root, root.val)

def unival_helper(root, val):
    if root is None:
        return True
    if root.val == val:
        return unival_helper(root.left, val) and unival_helper(root.right, val)
    return False

def count_unival_subtree(root):
    if root is None:
        return 0
    #print(root.val)
    left = count_unival_subtree(root.left)
    right = count_unival_subtree(root.right)

    return 1+left+right if is_unival(root) else left+right


print(count_unival_subtree(a))


