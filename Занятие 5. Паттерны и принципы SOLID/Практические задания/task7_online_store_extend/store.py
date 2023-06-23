from abc import abstractmethod


class ProductManagement:
    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def update_product(self, product):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass


class OrderManagement:
    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity


class ProductRepository:
    def add_product(self, product):
        # реализация для добавления продукта в репозиторий
        pass

    def update_product(self, product):
        # реализация для обновления продукта в репозитории
        pass

    def get_product(self, product_id):
        # реализация для извлечения продукта из репозитория
        pass


class OrderRepository:
    def place_order(self, order):
        # реализация для размещения заказа в репозитории
        pass

    def get_order(self, order_id):
        # реализация для извлечения заказа из репозитория
        pass


# Реализация принципа инверсии зависимостей путем введения классов репозитория в качестве зависимостей
class OnlineStore(ProductManagement, OrderManagement):
    def __init__(self, product_repository, order_repository):
        self.product_repository = product_repository
        self.order_repository = order_repository

    def add_product(self, product):
        self.product_repository.add_product(product)

    def update_product(self, product):
        self.product_repository.update_product(product)

    def get_product(self, product_id):
        return self.product_repository.get_product(product_id)

    def place_order(self, order):
        self.order_repository.place_order(order)

    def get_order(self, order_id):
        return self.order_repository.get_order(order_id)