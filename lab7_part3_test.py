import unittest
from lab7_part2 import calculate_min_cable, process_file_data


class TestCableNetwork(unittest.TestCase):
    """
    Class with tests of length cable network.
    """

    def test_simple_case(self):
        """
        Test, which process the simple case.
        """
        data = [("К1", "К2", 100), ("К2", "К3", 200), ("К1", "К3", 300)]
        result = calculate_min_cable(data)
        self.assertEqual(result, 300)

    def test_error_case(self):
        """
        Test, which process the error case.
        """
        data = [("К1", "К2", 10), ("К3", "К4", 20)]
        result = calculate_min_cable(data)
        self.assertEqual(result, -1)

    def test_csv_file_case(self):
        """
        Test, which process the case of csv file.
        """
        file_name = "communication_wells.csv"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("K1, K2, 2000 \n K2, K3, 1500 \n"
                       " K1, K3, 4000 \n K3, K4, 2500")
        result = process_file_data(file_name)
        self.assertEqual(result, 6000)


if __name__ == "__main__":
    unittest.main()
