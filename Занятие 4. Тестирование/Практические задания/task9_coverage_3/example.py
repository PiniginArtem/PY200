from typing import Optional, List


class SuperFunction:
    def __init__(self, data: Optional[List] = None):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if value is None:
            self._data = []
        else:
            self._data = value

    def append(self, value):
        if isinstance(value, (int, float, str)):
            self._data.append(value)
        else:
            raise TypeError("Не того типа")

    @staticmethod
    def sum_value(*args):
        if not all(map(lambda x: isinstance(args[0], type(x)), args[:-1])):
            raise TypeError("объекты разного типа")
        return sum(*args)

    def __str__(self):
        return f"Дата = {self.data}"

    def __repr__(self):
        return f"{self.__class__.__name__}(data={self.data})"


# if __name__ == "__main__":
#     s = SuperFunction()
#     s.append(4)
#     print(s.data)
#     print(s)
