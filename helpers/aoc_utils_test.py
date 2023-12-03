import unittest

from helpers.aoc_utils import get_adjacent_and_diagonal_coords


class TestDay03(unittest.TestCase):

    def test_adj_and_diag_corners(self):
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(0, 0)], 3, 3), [(0, 1), (1, 0), (1, 1)])
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(2, 0)], 3, 3), [(1, 0), (2, 1), (1, 1)])

        self.assertCountEqual(get_adjacent_and_diagonal_coords([(0, 2)], 3, 3), [(1, 1), (1, 2), (0, 1)])
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(2, 2)], 3, 3), [(2, 1), (1, 1), (1, 2)])
    
    def test_adj_diag_middle(self):
        self.assertCountEqual(get_adjacent_and_diagonal_coords([(1, 1)], 3, 3), [(0, 0), (0,1), (0,2), (1, 0), (1, 2), (2, 0), (2, 1), (2,2)])




if __name__ == '__main__':
    unittest.main()
