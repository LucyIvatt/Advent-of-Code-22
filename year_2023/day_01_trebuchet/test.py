import unittest

from year_2023.day_01_trebuchet.solution import answer, find_numbers
from utils.file_utils import input_data

class TestDay01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_01_trebuchet/example.txt")
        cls.example2 = input_data("year_2023/day_01_trebuchet/example2.txt")
        cls.puzzle_input = input_data("year_2023/day_01_trebuchet/input.txt")

    def test_p1_example(self):
        """
        Tests Day 01 Part 1 using the example given in the scenario
        """
        self.assertEqual(answer(self.__class__.example), 142)

    def test_p1_actual(self):
        """
        Tests the Day 01 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(answer(self.__class__.puzzle_input), 54081)

    def test_p2_example(self):
        """
        Tests Day 01 Part 2 using the example given in the scenario.
        """
        self.assertEqual(answer(self.__class__.example2, True), 281)

    def test_p2_actual(self):
        """
        Tests the Day 01 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(answer(self.__class__.puzzle_input, True), 54649)
    
    def test_find_number_locations(self):
        self.assertEqual(find_numbers('two1nine', True), ['2', '1', '9'])
        self.assertEqual(find_numbers('eightthree3ninekzhtlqsevenssprmrqhhgncrs', True), ['8', '3', '3', '9', '7'])
        self.assertEqual(find_numbers('sevennine3', True), ['7', '9', '3'])


if __name__ == '__main__':
    unittest.main()
