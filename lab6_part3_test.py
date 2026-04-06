import unittest
from lab6_part3 import parse_pref, calculate_min_beers


class TestBeerProblem(unittest.TestCase):
    """
    Unit tests for the Beer Choice Problem logic.
    Verifies that the algorithm correctly identifies the minimum number of beer types.
    """
    def test_1(self):
        """
        Test case № 1.
        """
        n, b = 2, 2
        pref_str = "YNNY"
        matrix = parse_pref(n, b, pref_str)
        result = calculate_min_beers(n, b, matrix)
        self.assertEqual(result, 2)


    def test_2(self):
        """
        Test case № 2.
        """
        n, b = 6, 3
        pref_str = "YNNYNYYNYNYYNYYNYN"
        matrix = parse_pref(n, b, pref_str)
        result = calculate_min_beers(n, b, matrix)
        self.assertEqual(result, 2)


    def test_3(self):
        """
        Test case № 3.
        """
        n, b = 2, 1
        pref_str = "YN"
        matrix = parse_pref(n, b, pref_str)
        result = calculate_min_beers(n, b, matrix)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
