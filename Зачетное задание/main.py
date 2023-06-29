import random
import hashlib
import re
from faker import Faker
from faker_food import FoodProvider


class IdCounter:
    """Класс, в котором хранится последниый сгенерированный id и генератор новых значений id."""
    def __init__(self):
        self.id = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    def get_new_id(self):
        self.id += 1
        return self.id


class Password:

    password_pattern = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]).{8,}")

    @classmethod
    def get_hash(cls, password: str) -> str:
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()
        raise TypeError("Bad password")

    @classmethod
    def is_valid(cls, password: str) -> bool:
        if cls.password_pattern.fullmatch(password):
            return True
        raise ValueError("Пароль должен соотвествовать условиям")

    @classmethod
    def check_password(cls, old_hash, password: str) -> bool:
        if old_hash == cls.get_hash(password):
            return True
        raise ValueError("Неправильно введён пароль")


class Product:
    id_counter = IdCounter()

    def __init__(self, name, price, rating):
        self.__id = self.__class__.id_counter.get_new_id()
        self.name = name
        self.price = None
        self.set_price(price)
        self.rating = None
        self.set_rating(rating)

    def set_price(self, price: float):
        if not isinstance(price, float):
            raise TypeError("Цена(price) должна быть типа float")
        if price == 0:
            raise ValueError("Товар не должен стоить 0")
        elif price < 0:
            raise ValueError("Цена не может быть отрицаительной")
        self.price = price

    def set_rating(self, rating: int):
        if not isinstance(rating, int):
            raise TypeError("Рейтинг(rating) должен быть типа int или float")
        if rating < 0:
            raise ValueError("Рейтинг не может быть отрицательным")
        self.rating = rating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Имя(name) должно быть типа str")
        self._name = name

    def __str__(self):
        return f'Товар #{self.__id} "{self.name}". Цена: {self.price} руб.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, rating={self.rating!r})'


class Cart:
    def __init__(self):
        self.cart = []

    def add(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('Добавляемый предмет должен быть типа "Product"')
        self.cart.append(product)

    def remove(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('Удаляемый предмет должен быть типа "Product"')
        if product in self.cart:
            self.cart.remove(product)
            print(f"Товар {product} удалён из корзины")
        else:
            print("Такого товара в корзине нет")

    def get_data(self) -> list[Product]:
        return self.cart


class User:
    id_counter = IdCounter()
    user_password = Password()

    def __init__(self, username, password):

        self._id = self.id_counter.get_new_id()
        self.__password = self.__class__.user_password.get_hash(password)
        self.cart = Cart()
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        self._username = username

    @property
    def username(self):
        return self._username

    def __str__(self):
        return f'Пользователь #{self._id}_"{self._username}".'

    def __repr__(self):
        return f'{self.__class__.__name__}(username={self._username!r}, password="password{self._id}")'


class ItemGenerator:
    """
    Генератор товаров продуктового магазина "Фрукты"
    """
    fake = Faker()
    fake.add_provider(FoodProvider)

    @staticmethod
    def get_rating() -> int:
        rating = random.randint(1, 10)
        return rating

    @staticmethod
    def get_price() -> float:
        price = random.random() * random.randint(1000, 3000)
        return round(price, 2)

    def get_random_item(self):
        while True:
            random_tool = {
                'name': self.__class__.fake.fruit(),
                'price': self.get_price(),
                'rating': self.get_rating()
            }
            return random_tool


class Store:
    item_gen = ItemGenerator()

    def __init__(self, number_of_goods: int):
        self.user = None
        self._authentification()
        self.list_goods = self._init_list_goods(number_of_goods)

    def _authentification(self):
        login = input("Введите Имя пользователя:\n")
        while True:
            password = input("Создайте новый пароль:\n"
                             "- длина должна быть не менее 8 символов \n"
                             "- содержать латинские буквы нижнего и верхенго регистра\n"
                             "- содержать спецсимвол\n"
                             )
            try:
                self.user = User(login, password)
                print("Пользователь успешно создан, добро пожаловать в магазин.")
                break
            except ValueError:
                print("Неправильно введён пароль")
                continue

    @classmethod
    def _init_list_goods(cls, number_of_goods: int) -> list[Product]:
        list_ = []
        for i in range(number_of_goods):
            list_.append(Product(**cls.item_gen.get_random_item()))
        return list_

    def print_list_goods(self):
        for good in self.list_goods:
            print(good)

    def add_to_cart(self, number: int):
        product = self.list_goods[number - 1]
        self.user.cart.add(product)
        print(f"Товар {product} добавлен в корзину")

    def view_cart(self):
        print(self.user.cart.get_data())


def run():
    print("Для того, чтобы войти в магазин необходимо создать нового пользовотеля!")
    st = Store(10)
    st.print_list_goods()
    while True:
        action_number = int(input("Введите номер действия:\n"
                                  "1. Показать продукты в магазине\n"
                                  "2. Добавить товар в корзину\n"
                                  "3. Показать корзину\n"
                                  "4. Удалить товар из корзины\n"
                                  "5. Оформить заказ\n"))
        if action_number == 1:
            st.print_list_goods()
        elif action_number == 2:
            st.add_to_cart(int(input("Введите номер товара, который хотите добавить в корзину\n")))
            continue
        elif action_number == 3:
            if st.user.cart.get_data():
                print(f"Корзина: {st.user}")
                for item in st.user.cart.get_data():
                    print(item)
            else:
                print("Корзина пуста!")
            continue
        elif action_number == 4:
            item_ = int(input("Введите номер товара, который хотите удалить из корзины\n"))
            st.user.cart.remove(st.list_goods[item_ - 1])
        elif action_number == 5:
            print("Заказ успешно оформлен!")
            break
        else:
            print("Введите корректное значение!")


if __name__ == "__main__":
    run()
