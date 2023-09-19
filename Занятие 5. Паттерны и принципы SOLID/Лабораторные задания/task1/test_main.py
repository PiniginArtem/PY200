import unittest
from main import StorageTransaction, OnlinePayment, CashPayment


class TestStorege(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.st = StorageTransaction()

    def test_add_transaction(self):
        with self.assertRaises(TypeError):
            self.st.add_transaction("123")

        trans_1 = OnlinePayment(1, 250)
        self.st.add_transaction(trans_1)
        self.assertEqual(self.st.transactions[0], trans_1)

    def test_check_transaction(self):
        self.st.add_transaction(CashPayment(12, 5, 10))
        self.assertTrue(self.st.check_transaction(12))

        self.st.add_transaction(CashPayment(13, 5, 1))
        self.assertFalse(self.st.check_transaction(13))

    def test_repeat_transaction(self):
        self.st.transactions[2].cash = 20
        self.assertFalse(self.st.transactions[2].successful_payment)
        self.st.repeat_transaction(13)
        self.assertTrue(self.st.transactions[2].successful_payment)

    def test_give_transaction(self):
        self.assertEqual(self.st.give_transaction_is_false(), [])
        self.st.add_transaction(CashPayment(14, 5, 1))
        self.assertEqual(self.st.give_transaction_is_false(), [14])


if __name__ == '__main__':
    unittest.main()
