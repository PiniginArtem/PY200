import unittest


def add(x, y):
    return x + y


class TestSum(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(add(1, 2), 3)  # верно

    def test_add2(self):
        self.assertEqual(add(-1, 1), 4)  # ошибка

    def test_add3(self):
        self.assertEqual(add(-1, -1), -8)  # ошибка

    def test_add4(self):
        self.assertEqual(add(1, 2), 3) # верно


if __name__ == '__main__':
    unittest.main()