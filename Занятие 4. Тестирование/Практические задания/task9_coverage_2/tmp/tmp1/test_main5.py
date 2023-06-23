import unittest
from example import SuperFunction


class MyTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(SuperFunction().data, [])

    def test_2(self):
        self.assertEqual(SuperFunction([1, 2, 3]).data, [1, 2, 3])

    def test_3(self):
        test = SuperFunction([1, 2, 3])
        test.append(4)
        self.assertEqual(test.data, list(range(1, 5)))

    def test_4(self):
        with self.assertRaises(TypeError):
            SuperFunction([1, 2, 3]).append([4])
