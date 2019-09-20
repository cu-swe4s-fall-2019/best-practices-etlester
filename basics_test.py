import sys
import unittest
import get_column_stats as cs
import random
import os
import math


class TestColumn(unittest.TestCase):
    def test_mean(self):
        file_mean = cs.col_mean(self.file_int)
        self.assertEqual(file_mean, self.direct_mean_int)

    def test_stdev(self):
        file_stdev = cs.col_stdev(self.file_int)
        self.assertEqual(file_stdev, self.direct_stdev_int)

    def test_mean_with_NaNs(self):
        bad_file = [2, 2, 2, 2, 2, 2, 'NaN']
        with self.assertRaises(TypeError):
            cs.col_mean(bad_file)

    def test_mean_with_non_int(self):
        bad_file = [2, 2, 'q', 2, 'a', 2]
        with self.assertRaises(TypeError):
            cs.col_mean(bad_file)

    def test_stdev_with_NaNs(self):
        bad_file = [2, 2, 2, 2, 2, 2, 'NaN']
        with self.assertRaises(TypeError):
            cs.col_stdev(bad_file)

    def test_stdev_with_non_int(self):
        bad_file = [2, 2, 'q', 2, 'a', 2]
        with self.assertRaises(TypeError):
            cs.col_stdev(bad_file)

    def setUp(self):
        self.direct_sum_int = 0
        self.file_int = []
        for i in range(100):
            rand_int = random.randint(1, 1000)
            self.direct_sum_int += rand_int
            self.file_int.append(rand_int)
        self.direct_mean_int = self.direct_sum_int/100
        self.direct_stdev_int = math.sqrt(sum([(self.direct_mean_int-x)**2
                                          for x in self.file_int]) /
                                          len(self.file_int))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
