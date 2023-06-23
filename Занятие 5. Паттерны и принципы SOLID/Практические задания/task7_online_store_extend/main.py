from store import OnlineStore


class CustomerRepository:
    def add_customer(self, customer):
        # реализация для добавления клиента в репозиторий
        pass

    def update_customer(self, customer):
        # реализация для обновления клиента в репозитории
        pass

    def get_customer(self, customer_id):
        # реализация для извлечения клиента из репозитория
        pass


# Добавление функциональности управления клиентами в класс OnlineStore
class OnlineStoreWithCustomers(OnlineStore):
    def __init__(self, product_repository, order_repository, customer_repository):
        super().__init__(product_repository, order_repository)
        self.customer_repository = customer_repository

    def add_customer(self, customer):
        self.customer_repository.add_customer(customer)

    def update_customer(self, customer):
        self.customer_repository.update_customer(customer)

    def get_customer(self, customer_id):
        return self.customer_repository.get_customer(customer_id)


if __name__ == "__main__":
    # Write your solution here
    pass
