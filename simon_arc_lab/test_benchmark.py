import unittest
import numpy as np
from .benchmark import *

class TestBenchmark(unittest.TestCase):
    def test_image_size1d_to_string(self):
        self.assertEqual(image_size1d_to_string(0), 'small')
        self.assertEqual(image_size1d_to_string(10), 'small')
        self.assertEqual(image_size1d_to_string(11), 'medium')
        self.assertEqual(image_size1d_to_string(20), 'medium')
        self.assertEqual(image_size1d_to_string(21), 'large')
        self.assertEqual(image_size1d_to_string(30), 'large')
        self.assertEqual(image_size1d_to_string(31), 'other')

    def test_histogram_total_to_string(self):
        self.assertEqual(histogram_total_to_string(0), 'a')
        self.assertEqual(histogram_total_to_string(10), 'a')
        self.assertEqual(histogram_total_to_string(11), 'b')
        self.assertEqual(histogram_total_to_string(100), 'b')
        self.assertEqual(histogram_total_to_string(101), 'c')
        self.assertEqual(histogram_total_to_string(1000), 'c')
        self.assertEqual(histogram_total_to_string(1001), 'd')
        self.assertEqual(histogram_total_to_string(10000), 'd')
        self.assertEqual(histogram_total_to_string(10001), 'e')
        self.assertEqual(histogram_total_to_string(100000), 'e')
        self.assertEqual(histogram_total_to_string(100001), 'other')
