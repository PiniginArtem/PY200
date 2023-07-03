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
        """
        Фунция, которая создаёт новый id, путём добавления 1 к старому, и сохраняет его как текущий
        :return: новый id
        """
        self.id += 1
        return self.id


class Password:
    """
    Класс, в котором производятся действия с паролем
    """

    # Паттерн для проверки пароля
    password_pattern = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]).{8,}")

    @classmethod
    def get_hash(cls, password: str) -> str:
        """
        Функция, которая возвращает хэш от пароля
        :param password: Пароль типа str
        :return: хэш от пароля
        """
        if cls.is_valid(password):
            return hashlib.sha256(password.encode()).hexdigest()
        raise ValueError("Bad password")

    @classmethod
    def is_valid(cls, password: str) -> bool:
        """
        Функция, которая проверяет пароль на вводимые символы
        :param password: Пароль типа str
        :return: True, если пароль подходит под паттерн. False, если нет
        """
        if cls.password_pattern.fullmatch(password):
            return True
        return False

    @classmethod
    def check_password(cls, old_hash: str, password: str) -> bool:
        """
        Функция, которая сверяет пароль с имеющимся хэшем.
        :param old_hash: Хэш, который был сохранен ранее
        :param password: Пароль, который вводят
        :return: True, если пароль подходит
        """
        if old_hash == cls.get_hash(password):
            return True
        raise ValueError("Неправильно введён пароль")


class Product:
    """
    Класс "Карточка товара", в котором содержится id, name, price, rating, соотвествующие одному товару
    """
    id_counter = IdCounter()

    def __init__(self, name, price, rating):
        self.__id = self.__class__.id_counter.get_new_id()
        self.name = name
        self.price = None
        self.set_price(price)
        self.rating = None
        self.set_rating(rating)

    def set_price(self, price: float):
        """
        Проводит проверки правильности введёной цены, и задаёт соотвествующий параметр класса
        :param price: Цена для товара в классе
        """
        if not isinstance(price, float):
            raise TypeError("Цена(price) должна быть типа float")
        if price == 0:
            raise ValueError("Товар не должен стоить 0")
        elif price < 0:
            raise ValueError("Цена не может быть отрицаительной")
        self.price = price

    def set_rating(self, rating: int):
        """
        Проводит проверки правильности введёного рейтинга, и задаёт соотвествующий параметр класса
        :param rating: Рейтинг для товара в классе
        """
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
    """
    Класс "Корзина" в интернет магазине
    """
    def __init__(self):
        self.cart = []

    def add(self, product: Product) -> None:
        """
        Добавляем карточку продукта в корзину, корточка должна быть типа Product
        :param product: Карточка продукта типа Product
        """
        if not isinstance(product, Product):
            raise TypeError('Добавляемый предмет должен быть типа "Product"')
        self.cart.append(product)

    def remove(self, product: Product) -> None:
        """
        Удаляем карточку продукта из корзины, корточка должна быть типа Product
        :param product: Карточка продукта типа Product
        """
        if not isinstance(product, Product):
            raise TypeError('Удаляемый предмет должен быть типа "Product"')
        if product in self.cart:
            self.cart.remove(product)
            print(f"Товар {product} удалён из корзины")
        else:
            print("Такого товара в корзине нет")

    def get_data(self) -> list[Product]:
        """
        Удаляем карточку продукта из корзины, корточка должна быть типа Product
        :return: Возвращает
        """
        return self.cart


class User:
    """
    Объект "Пользователь", в котором хранится информация: Имя, id, хэш пароля
    """

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
    Генератор случайных товаров
    """

    @staticmethod
    def get_rating() -> int:
        rating = random.randint(1, 10)
        return rating

    @staticmethod
    def get_price() -> float:
        price = random.random() * random.randint(1000, 3000)
        return round(price, 2)

    def get_random_item(self, func) -> dict:
        random_tool = {
            'name': func(),
            'price': self.get_price(),
            'rating': self.get_rating()
        }
        return random_tool


class Store:
    """
    Класс "Магазин фруктов"
    """

    fake = Faker()
    fake.add_provider(FoodProvider)
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
            list_.append(Product(**cls.item_gen.get_random_item(cls.fake.fruit)))
        return list_

    def print_list_goods(self):
        for good in self.list_goods:
            print(good)

    def add_to_cart(self, number: int):
        product = self.list_goods[number - 1]
        self.user.cart.add(product)
        print(f"Товар {product} добавлен в корзину")

    def view_cart(self):
        if self.user.cart.get_data():
            print(f"Корзина: {self.user}")
            for item in self.user.cart.get_data():
                print(item)
        else:
            print("Корзина пуста!")


class FruitStore:

    def __init__(self, number_of_goods: int):
        if not isinstance(number_of_goods, int):
            raise TypeError("Количество товаров в магазине должно быть типа int")
        if number_of_goods <= 0:
            raise ValueError("Количество товаров в магазине целым числом больше 0")
        print("Для того, чтобы войти в магазин необходимо создать нового пользовотеля!")
        self.store = Store(number_of_goods)

    def run(self):
        self.store.print_list_goods()
        while True:
            action_number = int(input("Введите номер действия:\n"
                                      "1 Показать продукты в магазине\n"
                                      "2 Добавить товар в корзину\n"
                                      "3 Показать корзину\n"
                                      "4 Удалить товар из корзины\n"
                                      "5 Оформить заказ\n"))
            if action_number == 1:
                self.store.print_list_goods()
            elif action_number == 2:
                self.store.add_to_cart(int(input("Введите номер товара, который хотите добавить в корзину\n")))
                continue
            elif action_number == 3:
                self.store.view_cart()
                continue
            elif action_number == 4:
                item_ = int(input("Введите номер товара, который хотите удалить из корзины\n"))
                self.store.user.cart.remove(self.store.list_goods[item_ - 1])
            elif action_number == 5:
                print("Заказ успешно оформлен!")
                break
            else:
                print("Введите корректный номер операции!")


if __name__ == "__main__":
    FruitStore(10).run()  # Инициализация магазина с 10 случайными товарами и его запуск
