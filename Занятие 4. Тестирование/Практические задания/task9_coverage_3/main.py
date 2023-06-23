import coverage
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


if __name__ == '__main__':
    unittest.main()
    # cov = coverage.Coverage()
    # cov.start()
    # # загрузка тестов из модуля
    # tests = unittest.TestLoader().loadTestsFromModule(MyTests)
    # # запуск тестов
    # unittest.TextTestRunner().run(tests)
    # unittest.main()
    # cov.stop()
    # cov.save()
    # cov.report()
