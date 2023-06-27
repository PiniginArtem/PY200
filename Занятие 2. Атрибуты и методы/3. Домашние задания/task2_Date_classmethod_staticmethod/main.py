class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

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
    def is_valid_date(cls, day: int, month: int, year: int) -> bool:
        """Проверяет, является ли дата корректной"""
        ...  # TODO проверить валидность даты
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError
        if not 1 <= day <= 31 or not 1 <= month <= 12 or not 0 <= year:
            return False
        if cls.is_leap_year(year):
            if day > cls.DAY_OF_MONTH[1][month - 1]:
                return False
        else:
            if day > cls.DAY_OF_MONTH[0][month - 1]:
                return False
        return True


if __name__ == "__main__":
    date = Date(11, 1, 2022)
    print(date.is_leap_year(2022))  # False
    print(date.get_max_day(11, 2000))  # 30
    print(date.is_valid_date(29, 2, 2020))  # True
    print(date.is_valid_date(29, 2, 2022))  # False
