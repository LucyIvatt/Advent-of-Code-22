import unittest

# TODO: import other solution methods
from python.year_2022.day_13_distress_signal.solution import Packet, input_data, part_one, part_two


class TestDay13(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_13_distress_signal"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_compare_basic(self):
        # Basic ints
        self.assertEqual(Packet.compare(1, 2), 1)
        self.assertEqual(Packet.compare(2, 2), 0)
        self.assertEqual(Packet.compare(2, 1), -1)

        # Basic lists - right list bigger
        self.assertEqual(Packet.compare([1, 2], [2, 3, 4]), 1)
        self.assertEqual(Packet.compare([1, 5], [2, 4, 2]), 1)
        self.assertEqual(Packet.compare([3, 2], [2, 3, 4]), -1)

        # Basic lists - left list bigger
        self.assertEqual(Packet.compare([1, 2, 3], [2, 3]), 1)
        self.assertEqual(Packet.compare([1, 2, 3], [0, 1]), -1)
        self.assertEqual(Packet.compare([1, 2, 3], [1, 2]), -1)

        # Basic lists - list same length
        self.assertEqual(Packet.compare([1, 2], [1, 3]), 1)
        self.assertEqual(Packet.compare([1, 2], [1, 2]), 0)
        self.assertEqual(Packet.compare([2, 2], [1, 2]), -1)

        # Int left, list right
        self.assertEqual(Packet.compare(1, [1, 2]), 1)
        self.assertEqual(Packet.compare(3, [1]), -1)
        self.assertEqual(Packet.compare(2, [2]), 0)

        # List left, int right
        self.assertEqual(Packet.compare([1], 2), 1)
        self.assertEqual(Packet.compare([3], 2), -1)
        self.assertEqual(Packet.compare([2], 2), 0)

    def test_day_13_p1_example(self):
        """
        Tests Day 13 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.example), 13)

    def test_day_13_p1_actual(self):
        """
        Tests the Day 13 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.input), 5717)

    def test_day_13_p2_example(self):
        """
        Tests Day 13 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.example), 140)

    def test_day_13_p2_actual(self):
        """
        Tests the Day 13 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.input), 25_935)


if __name__ == '__main__':
    unittest.main()
