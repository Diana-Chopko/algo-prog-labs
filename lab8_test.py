from lab8_algo import max_wire_len
import unittest


class TestWireLen(unittest.TestCase):
    """
    Class of test cases.
    """
    def test_case1(self):
        """
        The first test case.
        """
        w = 2
        height = [3, 3, 3]
        result = max_wire_len(w, height)
        self.assertEqual(result, 5.66)


    def test_case2(self):
        """
        The second test case.
        """
        w = 100
        height = [1, 1, 1, 1]
        result = max_wire_len(w, height)
        self.assertEqual(result, 300)


    def test_case3(self):
        """
        The third test case.
        """
        w = 4
        height = [100, 2, 100, 2, 100]
        result = max_wire_len(w, height)
        self.assertEqual(result, 396.32)


    def test_case4(self):
        """
        The fourth test case.
        """
        w = 4
        height = [
            56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5,
            91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51,
            34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72
        ]
        result = max_wire_len(w, height)
        self.assertEqual(result, 2738.18)


if __name__ == "__main__":
    unittest.main()