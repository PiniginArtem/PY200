import unittest


class MyClass(list):
    ...


class TestMyClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # Определили данные для тестов один раз для всех
        print("setUpClass")
        cls.my_list = MyClass()

    @classmethod
    def tearDownClass(cls):  # Очистили после всех тестов
        print("tearDownClass")
        cls.my_list.clear()

    def test_case_append(self):
        print("test_case_append")
        self.my_list.append(1)
        self.assertEqual(self.my_list, [1])

    def test_case_extend(self):
        print("test_case_extend")
        self.my_list.extend([2, 3, 4])
        self.assertEqual(self.my_list, list(range(1, 5)))

    def test_case_pop(self):
        print("test_case_pop")
        self.my_list.pop()
        self.assertEqual(self.my_list, list(range(1, 4)))

    def test_case_pop_again(self):
        print("test_case_pop_again")
        self.assertEqual(self.my_list.pop(), 3)

    def test_case_view(self):
        print("test_case_view")
        self.assertEqual(self.my_list, [1, 2])


if __name__ == '__main__':
    unittest.main()
