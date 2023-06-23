import unittest


class Calculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


def setUpModule():
    print("setUpModule")
    global calculator
    calculator = Calculator()


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = calculator.subtract(4, 2)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = calculator.divide(8, 2)
        self.assertEqual(result, 4)
        self.assertRaises(ValueError, calculator.divide, 8, 0)


if __name__ == '__main__':
    unittest.main()
