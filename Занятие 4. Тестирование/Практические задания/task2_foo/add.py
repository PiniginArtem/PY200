class Calculator:
    color = 'black'

    def __init__(self, base_value):
        self.value = base_value

    def iadd(self, value):
        self.value += value

    @classmethod
    def set_color(cls, value):
        cls.color = value

    @staticmethod
    def add(value1, value2):
        return value1 + value2
