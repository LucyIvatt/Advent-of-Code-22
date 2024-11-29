import unittest

from day08.solution import input_data, solution


class TestDay8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day08/example.txt")
        cls.input = input_data("day08/input.txt")

    def test_day_8_p1_example(self):
        """
        Tests Day 8 Part 1 using the example given in the scenario
        """
        self.assertEquals(solution(self.__class__.example)[0], 21)

    def test_day_8_p1_actual(self):
        """
        Tests the Day 8 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEquals(solution(self.__class__.input)[0], 1_711)

    def test_day_8_p2_example(self):
        """
        Tests Day 8 Part 2 using the example given in the scenario.
        """
        self.assertEquals(solution(self.__class__.example)[1], 8)

    def test_day_8_p2_actual(self):
        """
        Tests the Day 8 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input)[1], 301_392)


if __name__ == '__main__':
    unittest.main()
