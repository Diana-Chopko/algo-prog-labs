import unittest
from lab2_part3 import find_board_size


class TestBoardSize(unittest.TestCase):
    """
    Unit tests for validating the square board size calculation logic.
    """
    def test_1(self):
        """
        Test Case 1.
        """
        self.assertEqual(find_board_size(10, 2, 3), 9)

    def test_2(self):
        """
        Test Case 2.
        """
        self.assertEqual(find_board_size(2, 1000000000, 999999999), 1999999998)

    def test_3(self):
        """
        Test Case 3.
        """
        self.assertEqual(find_board_size(4, 1, 1), 2)


if __name__ == "__main__":
    unittest.main()
