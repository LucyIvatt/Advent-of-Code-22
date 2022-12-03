import unittest

from day2.solution import input_data, part_1, part_2


class TestDay2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day2/example.txt")
        cls.input = input_data("day2/input.txt")

    def test_day_2_p1_example(self):
        """
        Tests Day 2 Part 1 using the example given in the scenario
        """
        answer = part_1(self.__class__.example)
        self.assertEqual(answer, 15)

    def test_day_2_p1_actual(self):
        """
        Tests the Day 2 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        answer = part_1(self.__class__.input)
        self.assertEqual(answer, 13_221)

    def test_day_2_p2_example(self):
        """
        Tests Day 2 Part 2 using the example given in the scenario.
        """
        answer = part_2(self.__class__.example)
        self.assertEqual(answer, 12)

    def test_day_2_p2_actual(self):
        """
        Tests the Day 2 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass


if __name__ == '__main__':
    unittest.main()
