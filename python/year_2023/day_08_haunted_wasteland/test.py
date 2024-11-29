import unittest

from python.year_2023.day_08_haunted_wasteland.solution import input_data, part_one, part_two


class TestDay08(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "python/year_2023/day_08_haunted_wasteland/example.txt")
        cls.example2 = input_data(
            "python/year_2023/day_08_haunted_wasteland/example2.txt")
        cls.example3 = input_data(
            "python/year_2023/day_08_haunted_wasteland/example3.txt")
        cls.puzzle_input = input_data(
            "python/year_2023/day_08_haunted_wasteland/input.txt")

    def test_p1_example(self):
        """
        Tests Day 08 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 2)

    def test_p1_example_2(self):
        """
        Tests Day 08 Part 1 using example 2 given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example2), 6)

    def test_p1_actual(self):
        """
        Tests the Day 08 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 22357)

    def test_p2_example(self):
        """
        Tests Day 08 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example3), 6)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 08 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input),
                         10_371_555_451_871)


if __name__ == '__main__':
    unittest.main()
