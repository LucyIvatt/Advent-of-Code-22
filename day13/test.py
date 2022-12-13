import unittest

# TODO: import other solution methods
from day13.solution import input_data, compare


class TestDay13(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day13/example.txt")
        cls.input = input_data("day13/input.txt")

    def test_compare(self):
        # Basic ints
        self.assertEqual(compare(1, 2), 1)
        self.assertEqual(compare(2, 2), 0)
        self.assertEqual(compare(2, 1), -1)

        # Basic lists - right list bigger
        self.assertEqual(compare([1, 2], [2, 3, 4]), 1)
        self.assertEqual(compare([3, 2], [2, 3, 4]), -1)

        # Basic lists - left list bigger
        self.assertEqual(compare([1, 2, 3], [2, 3]), -1)
        self.assertEqual(compare([1, 2, 3], [0, 1]), -1)
        self.assertEqual(compare([1, 2, 3], [1, 2]), -1)

        # Basic lists - list same length
        self.assertEqual(compare([1, 2], [1, 3]), 1)
        self.assertEqual(compare([1, 2], [1, 2]), 0)
        self.assertEqual(compare([2, 2], [1, 2]), -1)

        # Int left, list right
        self.assertEqual(compare(1, [1, 2]), 1)
        self.assertEqual(compare(3, [1]), -1)
        self.assertEqual(compare(2, [2]), 0)

        # List left, int right
        self.assertEqual(compare([1], 2), 1)
        self.assertEqual(compare([3], 2), -1)
        self.assertEqual(compare([2], 2), 0)

    def test_day_13_p1_example(self):
        """
        Tests Day 13 Part 1 using the example given in the scenario
        """
        pass

    def test_day_13_p1_actual(self):
        """
        Tests the Day 13 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_13_p2_example(self):
        """
        Tests Day 13 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_13_p2_actual(self):
        """
        Tests the Day 13 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass


if __name__ == '__main__':
    unittest.main()
