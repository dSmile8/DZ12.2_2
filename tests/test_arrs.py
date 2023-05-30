import unittest

from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], -1, "test"), "test")
        self.assertEqual(arrs.get([5, 8, 4, 6], 3, "test"), 6)
        self.assertEqual(arrs.get([5, 8, 4, 6], 1, "test"), 8)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, -1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 2), [2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 8, 6, 9], 0, -2), [1, 2, 8])
        self.assertEqual(arrs.my_slice([], 0, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -6,), [1, 2, 3, 4, 5])
