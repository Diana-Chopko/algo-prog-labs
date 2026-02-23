import unittest
from lab1_part3 import finding_unsorted_subarray


class TestUnsortedArray(unittest.TestCase):
    """
    This class contains test cases to verify the correct identification
    of the starting and ending indices of the shortest unsorted continuous
    subarray.
    """


    def test_from_task_array(self):
        """
        Test the function with the primary example array provided in the task.
        """
        example_array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(finding_unsorted_subarray(example_array), (3, 9))


    def test_already_sorted_array(self):
        """
        Test the function with an array that is already fully sorted in ascending order.
        """
        example_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(finding_unsorted_subarray(example_array), (-1, -1))


    def test_unsorted_array(self):
        """
        Test the function with a completely unsorted array.
        """
        example_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(finding_unsorted_subarray(example_array), (0, 8))


    def test_one_element_array(self):
        """
        Test the function with an array containing only a single element.
        """
        example_array = [77]
        self.assertEqual(finding_unsorted_subarray(example_array), (-1, -1))


if __name__ == "__main__":
    unittest.main()
