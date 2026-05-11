import unittest
from lab9_algo import kmp_search


class TestKMPSearch(unittest.TestCase):
    """
    Tests to check the correct operation of the KMP algorithm.
    """
    def test_single_occurrence(self):
        """
        The first test case.
        """
        self.assertEqual(kmp_search("hello world", "world"), [6])


    def test_multiple_occurrence(self):
        """
        The second test case.
        """
        self.assertEqual(kmp_search("ababa", "aba"), [0, 2])


    def test_no_occurrence(self):
        """
        The third test case.
        """
        self.assertEqual(kmp_search("abcdef", "xyz"), [])


    def test_empty_needle(self):
        """
        The fourth test case.
        """
        self.assertEqual(kmp_search("abcdef", ""), [])


    def test_overlapping(self):
        """
        The fifth test case.
        """
        self.assertEqual(kmp_search("aaaaa", "aa"), [0,1, 2, 3])


if __name__ == "__main__":
    unittest.main()
    