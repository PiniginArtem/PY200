import unittest


class MyClass(list):
    ...


class TestMyClass(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.my_list = MyClass() # Определили данные для тестов

    def tearDown(self):
        print("tearDown")
        self.my_list.clear() # Очистили после каждого теста

    def test_case_append(self):
        print("test_case_append")
        self.my_list.append(1)
        self.assertEqual(self.my_list, [1])

    def test_case_pop(self):
        print("test_case_IndexError")
        self.assertRaises(IndexError, lambda x: x.pop(), self.my_list)

    def test_case_pop1(self):
        print("test_case_IndexError1")
        with self.assertRaises(IndexError):
            self.my_list.pop()


if __name__ == '__main__':
    unittest.main()
