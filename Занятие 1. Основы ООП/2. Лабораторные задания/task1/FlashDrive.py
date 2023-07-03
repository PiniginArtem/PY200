class FlashDrive:
    def __init__(self, memory: int, occupied_space: int):
        """
        Создание и подготовка к работе объекта "Флешка"

        :param memory: Объем памяти флеш диска в байтах
        :param occupied_space: Объем занятой памяти флеш диска в байтах

        Примеры:
        >>> flash = FlashDrive(1024, 0)  # инициализация экземпляра класса
        """
        if type(memory) is not int:
            raise TypeError("Объем памяти флеш диска должен быть целым числом")
        if memory <= 0:
            raise ValueError("Объем памяти флеш диска должен быть положительным числом")
        self.memory = memory

        if type(occupied_space) is not int:
            raise TypeError("Объем занятой памяти должен быть целым числом")
        if occupied_space < 0:
            raise ValueError("Объем занятой памяти не может быть отрицательным числом")
        self.occupied_space = occupied_space

    def is_empty_flash_drive(self) -> bool:
        """
        Функция которая проверяет является ли флеш накопитель пустым

        :return: True, если флеш накопитель пустой

        Примеры:
        >>> flash = FlashDrive(1024, 0)
        >>> flash.is_empty_flash_drive()
        """
        ...

    def add_file_to_flash_drive(self, file_size: int) -> None:
        """
        Добавление файла на флеш накопитель.

        :param file_size: Объем добавляемого файла на флеш накопитель
        :raise ValueError: Если объем жобавляемого файла превышает свободное место в флеш накопителе,
        то вызываем ошибку

        Примеры:
        >>> flash = FlashDrive(1024, 0)
        >>> flash.add_file_to_flash_drive(128)
        """
        if type(file_size) is not int:
            raise TypeError("Объем добавляемого файла должен быть типа int")
        if 0 > file_size > (self.memory - self.occupied_space):
            raise ValueError("Объем добавляемого файла должен быть больше 0 и меньше свободного места"
                             "на флеш накопителе")
        ...

    def clear_flash_drive(self) -> bool:
        """
        Очистка флеш накопителя.

        :return: True, если очистка флеш накопителя прошла успешно

        Примеры:
        >>> flash = FlashDrive(1024, 515)
        >>> flash.clear_flash_drive()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
