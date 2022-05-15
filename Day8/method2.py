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


def count_unival_subtrees(root):
    count, _ = helper(root)
    return count


def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        return total_count+1, True

    return total_count, False



if __name__ == "__main__":
    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)
    a.right.left = Node(1)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)
    a.right.right = Node(0)

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

    print(count_unival_subtrees(a))

