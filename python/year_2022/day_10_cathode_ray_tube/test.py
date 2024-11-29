import unittest

from python.year_2022.day_10_cathode_ray_tube.solution import input_data, solution


class TestDay10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_10_cathode_ray_tube"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_10_p1_example(self):
        """
        Tests Day 10 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example)[0], 13_140)

    def test_day_10_p1_actual(self):
        """
        Tests the Day 10 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input)[0], 12_840)


if __name__ == '__main__':
    unittest.main()
