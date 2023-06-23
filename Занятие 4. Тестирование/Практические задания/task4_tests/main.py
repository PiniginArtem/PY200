import unittest


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_case_1(self):
        print("test_case_1")

    def test_case_2(self):
        print("test_case_2")


if __name__ == '__main__':
    unittest.main()
