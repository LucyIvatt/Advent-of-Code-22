import unittest

from python.year_2022.day_07_no_space_left_on_device.solution import input_data, solution


class TestDay7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_07_no_space_left_on_device"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_7_p1_example(self):
        """
        Tests Day 7 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example)[0], 95_437)

    def test_day_7_p1_actual(self):
        """
        Tests the Day 7 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input)[0], 1_334_506)

    def test_day_7_p2_example(self):
        """
        Tests Day 7 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.__class__.example)[1], 24_933_642)

    def test_day_7_p2_actual(self):
        """
        Tests the Day 7 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input)[1], 7_421_137)


if __name__ == '__main__':
    unittest.main()
