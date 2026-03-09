class BinaryTree:
    """
    Class, which represents a node in a binary tree.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(node):
    """
    Calculates the height of a binary tree if it is balanced.

    :param node: The root node of the binary tree or subtree.

    :return: height
    """
    if node is None:
        height = 0
    else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if -1 in [left_height, right_height] or abs(left_height - right_height) > 1:
            height = -1
        else:
            height = max(left_height, right_height) + 1

    return height


def is_tree_balanced(node: BinaryTree) -> bool:
    """
    Determines if a binary tree is height-balanced.

    :param node: The root node of the binary tree.

    :return: is_balanced
    """
    check_height = get_height(node)
    if check_height == -1:
        is_balanced = False
    else:
        is_balanced = True

    return is_balanced
