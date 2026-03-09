import unittest
from lab3_part3 import BinaryTree, is_tree_balanced


class Test(unittest.TestCase):
    """
    Unit tests for checking the balance of a binary tree.
    """
    def test_binary_tree(self):
        """
        Test a balanced binary tree structure.
        The tree structure:
              1
             / \
            2   3
           / \
          4   5
        """
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)

        self.assertTrue(is_tree_balanced(root))


if __name__ == "__main__":
    unittest.main()
