import unittest

from python.year_2022.day_11_monkey_in_the_middle.solution import input_data, solution


class TestDay11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_11_monkey_in_the_middle"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_11_p1_example(self):
        """
        Tests Day 11 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.example), 10_605)

    def test_day_11_p1_actual(self):
        """
        Tests the Day 11 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.input), 50_172)

    def test_day_11_p2_example(self):
        """
        Tests Day 11 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.example, part_two=True), 2_713_310_158)

    def test_day_11_p2_actual(self):
        """
        Tests the Day 11 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.input, part_two=True), 11_614_682_178)


if __name__ == '__main__':
    unittest.main()
