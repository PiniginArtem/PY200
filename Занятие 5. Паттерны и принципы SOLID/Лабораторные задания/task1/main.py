from abc import ABC, abstractmethod
from typing import Union


class Check(ABC):
    """
    Абстрактный класс для определения интерфейса выдачи чеков
    """
    @abstractmethod
    def submit_check(self):
        pass


class SendCheckEmail(Check):
    """
    Класс, который реализует отправку чека на электронную почту
    """
    def submit_check(self):
        """
        >>> SendCheckEmail().submit_check()
        Отправил чек на электронную почту
        """
        print("Отправил чек на электронную почту")


class PrintCheck(Check):
    """
    Класс, который реализует выдачу бумажного чека
    """
    def submit_check(self):
        """
        >>> PrintCheck().submit_check()
        Выдали бумажный чек
        """
        print("Выдали бумажный чек")


class Payments(ABC):
    """
    Абстрактный класс для описания общего случая платежа
    """
    def __init__(self, id_order: int, cost: Union[int, float]):

        if not isinstance(id_order, int):
            raise TypeError
        if id_order < 1:
            raise ValueError
        self.id_order = id_order

        if not isinstance(cost, (int, float)):
            raise TypeError
        if cost < 1:
            raise ValueError
        self.cost = cost

        self.successful_payment = False
        self.do_transaction()

    @abstractmethod
    def do_transaction(self):
        pass


class CashPayment(Payments, PrintCheck):
    """
    Класс оплата наличными средствами
    """
    def __init__(self, id_order: int, cost: Union[int, float], cash: Union[int, float]):
        """
        >>> CashPayment(1, "abc", 10)
        Traceback (most recent call last):
        ...
        TypeError
        >>> CashPayment(1, 5, 10).cost
        Выполняем операцию платежа по заказу 1...
        Операция успешна, ваша сдача: 5
        Выдали бумажный чек
        5
        >>> CashPayment(123, 5, 2).id_order
        Выполняем операцию платежа по заказу 123...
        Дали мало налички. Операция не проведена.
        123
        """
        if not isinstance(cash, (int, float)):
            raise TypeError
        if cash < 1:
            raise ValueError
        self.cash = cash
        super().__init__(id_order, cost)

    def do_transaction(self):
        """
        >>> CashPayment(1, 5, 10).do_transaction()
        Выполняем операцию платежа по заказу 1...
        Операция успешна, ваша сдача: 5
        Выдали бумажный чек
        Операция уже была проведена
        """
        if not self.successful_payment:
            print(f"Выполняем операцию платежа по заказу {self.id_order}...")
            if self.cash < self.cost:
                print("Дали мало налички. Операция не проведена.")
            else:
                self.successful_payment = True
                print(f"Операция успешна, ваша сдача: {self.cash - self.cost}")
                self.submit_check()
        else:
            print("Операция уже была проведена")


class OnlinePayment(Payments, SendCheckEmail):
    """
    Класс онлайн оплата
    """
    def __init__(self, id_order: int, cost: float):
        """
        >>> OnlinePayment(1, "abc")
        Traceback (most recent call last):
        ...
        TypeError
        >>> OnlinePayment(1, 5).cost
        Выполняем операцию платежа по заказу 1...
        Операция успешна.
        Отправил чек на электронную почту
        5
        >>> OnlinePayment(123, 5).id_order
        Выполняем операцию платежа по заказу 123...
        Операция успешна.
        Отправил чек на электронную почту
        123
        """
        super().__init__(id_order, cost)

    def do_transaction(self):
        """
        >>> OnlinePayment(1, 5).do_transaction()
        Выполняем операцию платежа по заказу 1...
        Операция успешна.
        Отправил чек на электронную почту
        Операция уже была проведена
        """
        if not self.successful_payment:
            print(f"Выполняем операцию платежа по заказу {self.id_order}...")
            self.successful_payment = True
            print(f"Операция успешна.")
            self.submit_check()
        else:
            print("Операция уже была проведена")


class StorageTransaction:
    """
    Хранение транзакций
    """
    def __init__(self):
        """
        >>> StorageTransaction().transactions
        []
        """
        self.transactions = []

    def add_transaction(self, transaction: Payments):
        """
        >>> storage.add_transaction("123")
        Traceback (most recent call last):
        ...
        TypeError
        >>> storage.add_transaction(CashPayment(12, 5, 10))
        Выполняем операцию платежа по заказу 12...
        Операция успешна, ваша сдача: 5
        Выдали бумажный чек
        >>> storage.add_transaction(CashPayment(13, 5, 1))
        Выполняем операцию платежа по заказу 13...
        Дали мало налички. Операция не проведена.
        """
        if not isinstance(transaction, Payments):
            raise TypeError
        self.transactions.append(transaction)

    def check_transaction(self, id: int) -> bool:
        """
        >>> storage.check_transaction(12)
        True
        >>> storage.check_transaction(13)
        False
        >>> storage.check_transaction(14)
        Платёж с таким id не найден
        """
        for transaction in self.transactions:
            if transaction.id_order == id:
                return transaction.successful_payment
        print(f"Платёж с таким id не найден")

    def repeat_transaction(self, id: int):
        """
        >>> storage.transactions[1].cash = 20
        >>> storage.repeat_transaction(13)
        Выполняем операцию платежа по заказу 13...
        Операция успешна, ваша сдача: 15
        Выдали бумажный чек
        """
        for transaction in self.transactions:
            if transaction.id_order == id:
                transaction.do_transaction()
                break
        else:
            print(f"Платёж с таким id не найден")

    def give_transaction_is_false(self) -> list:
        """
        >>> storage.give_transaction_is_false()
        [13]
        >>> storage.add_transaction(CashPayment(14, 5, 4))
        Выполняем операцию платежа по заказу 14...
        Дали мало налички. Операция не проведена.
        >>> storage.give_transaction_is_false()
        [13, 14]
        """
        list_ = []
        for transaction in self.transactions:
            if not transaction.successful_payment:
                list_.append(transaction.id_order)
        return list_


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'storage': StorageTransaction()})

    # st = StorageTransaction()
    # st.add_transaction(CashPayment(1, 5, 10))
    # st.add_transaction(OnlinePayment(2, 100))
    # st.add_transaction(CashPayment(3, 5, 4))
    # for tr in st.transactions:
    #     print(f"id = {tr.id_order}, {tr.successful_payment}")
    # print(st.give_transaction_is_false())
    # st.transactions[2].cash = 20
    # st.repeat_transaction(3)
    # for tr in st.transactions:
    #     print(f"id = {tr.id_order}, {tr.successful_payment}")
    # print(st.give_transaction_is_false())

