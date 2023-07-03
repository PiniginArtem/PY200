class Date:
    def __init__(self, day: int, month: int, year: int):
        if type(day) is not int or type(month) is not int or type(year) is not int:
            raise TypeError("День, месяц или год должны быть целыми числами")
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:0>4}"


if __name__ == "__main__":
    date1 = Date(1, 1, 2021)
    date2 = Date(11, 10, 1999)
    print(date1)
    print((date1, date2))
