import unittest

from python.year_2022.day_09_rope_bridge.solution import input_data, part_one, part_two, move_tail


class TestDay9(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_09_rope_bridge"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_move_tail_horizontal(self):
        self.assertEqual(move_tail((-2, 0), (0, 0)), (-1, 0))
        self.assertEqual(move_tail((2, 0), (0, 0)), (1, 0))
        self.assertEqual(move_tail((0, -2), (0, 0)), (0, -1))
        self.assertEqual(move_tail((0, 2), (0, 0)), (0, 1))

    def test_move_tail_diagonal(self):
        self.assertEqual(move_tail((-1, -2), (0, 0)), (-1, -1))
        self.assertEqual(move_tail((-2, -1), (0, 0)), (-1, -1))

        self.assertEqual(move_tail((-2, 1), (0, 0)), (-1, 1))
        self.assertEqual(move_tail((-1, 2), (0, 0)), (-1, 1))

        self.assertEqual(move_tail((1, 2), (0, 0)), (1, 1))
        self.assertEqual(move_tail((2, 1), (0, 0)), (1, 1))

        self.assertEqual(move_tail((2, -1), (0, 0)), (1, -1))
        self.assertEqual(move_tail((1, -2), (0, 0)), (1, -1))

    def test_move_tail_no_move(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.assertEqual(move_tail((i, j), (0, 0)), (0, 0))

    def test_day_9_p1_example(self):
        """
        Tests Day 9 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 13)

    def test_day_9_p1_actual(self):
        """
        Tests the Day 9 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.input), 6_243)

    def test_day_9_p2_example(self):
        """
        Tests Day 9 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 1)

    def test_day_9_p2_actual(self):
        """
        Tests the Day 9 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.input), 2_630)


if __name__ == '__main__':
    unittest.main()
