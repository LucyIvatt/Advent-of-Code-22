import unittest

from year_2023.day_04_scratchcards.solution import input_data, part_one, part_two

class TestDay04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_04_scratchcards/example.txt")
        cls.puzzle_input = input_data("year_2023/day_04_scratchcards/input.txt")

    def test_p1_example(self):
        """
        Tests Day 04 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 13)
        

    def test_p1_actual(self):
        """
        Tests the Day 04 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 17_782)

    def test_p2_example(self):
        """
        Tests Day 04 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 30)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 04 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 8477787)
        pass

if __name__ == '__main__':
    unittest.main()
