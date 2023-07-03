from typing import Optional
class PaperStickers:
    """
    Класс, "Стопка бумажных наклеек"
    """
    def __init__(self, paper_size: tuple, number_stickers: int, color: str = "yellow", adhesive_layer: Optional = True):
        """
        Создает объект "Стопка бумажных наклеек"

        :param paper_size: Размер листка
        :param number_stickers: Количество листков в стопке
        :param color: Цвет листков
        :param adhesive_layer: Липкий слой

        Примеры:
        >>> stickers = PaperStickers((50, 40), 100, "green", False)  # инициализация экземпляра класса
        """
        if not isinstance(paper_size, tuple):
            raise TypeError("Размер листка задаётся Кортежем из 2 чисел")
        if len(paper_size) != 2:
            raise ValueError("В Кортеже должно быть 2 числа, длина и ширина листка")
        self.paper_size = paper_size

        if type(number_stickers) is not int:
            raise TypeError("Количество листков в стопке должно быть целым числом")
        if number_stickers <= 0:
            raise ValueError("ОКоличество листков в стопке должно быть положительным числом")
        self.number_stickers = number_stickers

        if type(color) is not str:
            raise TypeError("Цвет листков задаётся строковым значением")
        self.color = color

        if type(adhesive_layer) is not bool:
            raise TypeError("Переменная adhesive_layer должно быть bool")
        self.adhesive_layer = adhesive_layer

    def write_note(self, number_of_sheets: int) -> None:
        """
        Берём number_of_sheets листков из стопки (уменьшаем кол-во листков в стопке на number_of_sheets)

        :param number_of_sheets: количество листков, которое хотим взять из стопки

        :raise ValueError: Если объем жобавляемого файла превышает свободное место в флеш накопителе,
        то вызываем ошибкуa

        Примеры:
        >>> stickers = PaperStickers((50, 40), 100, "green", False)
        >>> stickers.write_note(102)
        Traceback (most recent call last):
            ...
        ValueError: Кол-во листков, которое мы хотим взять, превышает кол-во оставшихся листков в пачке
        """
        if self.number_stickers < number_of_sheets:
            raise ValueError("Кол-во листков, которое мы хотим взять, превышает кол-во оставшихся листков в пачке")
        ...

    def remaining_number_sheets(self) -> int:
        """
        Возвращает кол-во оставшихся листков в пачке

        >>> stickers = PaperStickers((50, 40), 100, "green", False)
        >>> stickers.remaining_number_sheets()
        100
        """
        return self.number_stickers

    def color_sheets(self) -> str:
        """
        Возвращает цвет листко

        >>> stickers = PaperStickers((50, 40), 100, "green", False)
        >>> stickers.color_sheets()
        'green'
        """
        return self.color


if __name__ == "__main__":
    import doctest
    doctest.testmod()
