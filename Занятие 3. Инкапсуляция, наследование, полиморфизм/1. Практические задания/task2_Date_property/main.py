class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 100 != 0:
            return True if year % 4 == 0 else False
        else:
            return True if (year // 100) % 4 == 0 else False

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[1][month - 1]
        else:
            return cls.DAY_OF_MONTH[0][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError
        if not 1 <= day <= 31 or not 1 <= month <= 12 or not 0 <= year:
            raise ValueError
        if cls.is_leap_year(year):
            if day > cls.DAY_OF_MONTH[1][month - 1]:
                raise ValueError
        else:
            if day > cls.DAY_OF_MONTH[0][month - 1]:
                raise ValueError

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self.is_valid_date(value, self._month, self._year)
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self.is_valid_date(self._day, value, self._year)
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self.is_valid_date(self._day, self._month, value)
        self._year = value


if __name__ == "__main__":
    date = Date(5, 10, 2022)
    print(date.day)
    date.day = 31
    print(date.day)
    # date.day = 32  # ValueError

