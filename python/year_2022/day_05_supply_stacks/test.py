import unittest

from python.year_2022.day_05_supply_stacks.solution import input_data, solution


class TestDay5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_05_supply_stacks"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_5_p1_example(self):
        """
        Tests Day 5 Part 1 using the example given in the scenario
        """
        self.assertEqual(
            solution(self.__class__.example, old_model=True), "CMZ")

    def test_day_5_p1_actual(self):
        """
        Tests the Day 5 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input,
                         old_model=True), "FCVRLMVQP")

    def test_day_5_p2_example(self):
        """
        Tests Day 5 Part 2 using the example given in the scenario.
        """
        self.assertEqual(
            solution(self.__class__.example, old_model=False), "MCD")

    def test_day_5_p2_actual(self):
        """
        Tests the Day 5 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(
            solution(self.__class__.input, old_model=False), "RWLWGJGFD")


if __name__ == '__main__':
    unittest.main()
