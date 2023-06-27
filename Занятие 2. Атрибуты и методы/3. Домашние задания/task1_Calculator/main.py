class Calculator:
    @staticmethod
    def add(number_1: int, number_2: int) -> int:
        if not isinstance(number_1, int) or not isinstance(number_2, int):
            raise TypeError
        return number_1 + number_2

    @staticmethod
    def mul(number_1: int, number_2: int) -> int:
        if not isinstance(number_1, int) or not isinstance(number_2, int):
            raise TypeError
        return number_1 * number_2


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
