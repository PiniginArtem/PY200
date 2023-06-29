import random
import hashlib

class IdCounter:
    def __init__(self):
        pass
    def current_id(self):
        pass
    def get_new_id(self):
        return None

class Password:
    @classmethod
    def get(cls, password: str):
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()
        raise TypeError("jjfjjj")

    @staticmethod
    def is_valid(password):
        return True

    @classmethod
    def check(cls, password, hash_password):
        pass

class Product:
    _counter = IdCounter()

    def __init__(self, name, price, rating):
        self._id = self._counter.get_new_id()
        pass


class Cart:
    def __init__(self):
        self._data = []

    def add(self, product):
        self._data.append(product)

    def remove(self):
        pass

    def get_data(self):
        pass

class User:
    _counter = IdCounter()

    def __init__(self, username, password):

        self._id = self._counter.get_new_id()
        ...
        self.__password = Password.get(password)
        self._cart = Cart()


class Store:
    def __init__(self, product_generator):
        self.user = None
        self.authentification()
        self.product_generator = product_generator

    def authentification(self):
        while True:
            login = input()
            password = input()
        try:
            self.user = User(login, password)
            ...
    def add_to_cart(self):
        product = self.product_generator.get_product()
        self.user._cart.add(product)

    def view_cart(self):
        print(self.user.cart.get_data())

if __name__ == "__main__":
    st = Store(None)
    pr1 = Product(1,2,3)
    st.add_to_cart(pr1)
    st.view_cart()
