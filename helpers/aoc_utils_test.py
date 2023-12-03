import unittest

from helpers.aoc_utils import get_adjacent_coords


class AocUtilsTest(unittest.TestCase):

    def test_adj_diag_corners_single(self):
        self.assertCountEqual(get_adjacent_coords([(0, 0)], x_limit=3, y_limit=3, diagonal=True), [(0, 1), (1, 0), (1, 1)])
        self.assertCountEqual(get_adjacent_coords([(2, 0)], x_limit=3, y_limit=3, diagonal=True), [(1, 0), (2, 1), (1, 1)])
        self.assertCountEqual(get_adjacent_coords([(0, 2)], x_limit=3, y_limit=3, diagonal=True), [(1, 1), (1, 2), (0, 1)])
        self.assertCountEqual(get_adjacent_coords([(2, 2)], x_limit=3, y_limit=3, diagonal=True), [(2, 1), (1, 1), (1, 2)])
    
    def test_adj_corners_single(self):
        self.assertCountEqual(get_adjacent_coords([(0, 0)], x_limit=3, y_limit=3, diagonal=False), [(0, 1), (1, 0)])
        self.assertCountEqual(get_adjacent_coords([(2, 0)], x_limit=3, y_limit=3, diagonal=False), [(1, 0), (2, 1)])
        self.assertCountEqual(get_adjacent_coords([(0, 2)], x_limit=3, y_limit=3, diagonal=False), [(1, 2), (0, 1)])
        self.assertCountEqual(get_adjacent_coords([(2, 2)], x_limit=3, y_limit=3, diagonal=False), [(2, 1), (1, 2)])

    
    def test_adj_diag_middle_single(self):
        self.assertCountEqual(get_adjacent_coords([(1, 1)], x_limit=3, y_limit=3, diagonal=True), 
                                        [(0, 0), (0,1), (0,2), (1, 0), (1, 2), (2, 0), (2, 1), (2,2)])
        
    def test_adj_middle_single(self):
        self.assertCountEqual(get_adjacent_coords([(1, 1)], x_limit=3, y_limit=3, diagonal=False), 
                                        [(0,1), (1, 0), (1, 2), (2, 1)])
    
    def test_adj_diag_middle_multiple(self):
        self.assertCountEqual(get_adjacent_coords([(1, 1), (1,2)], x_limit=3, y_limit=4, diagonal=True), 
                                        [(0, 0), (1,0), (2,0), (0, 1), (0, 2), (0, 3), (1, 3), (2,3), (2, 1), (2, 2)])
    
    def test_adj_middle_multiple(self):
        self.assertCountEqual(get_adjacent_coords([(1, 1), (1,2)], x_limit=3, y_limit=4, diagonal=False), 
                                        [(1, 0), (2, 1), (2, 2), (1, 3), (0, 2), (0, 1)])

if __name__ == '__main__':
    unittest.main()
