from typing import Union, Optional


class FlashDrive:
    def __init__(self, memory: int, occupied_space: Optional[int] = 0):
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
        self._memory = memory
        self.occupied_space = occupied_space

    @property
    def memory(self):
        return self._memory

    @property
    def occupied_space(self) -> int:
        """Возвращает объем занятой памяти на флеш накопителе."""
        return self._occupied_space

    @occupied_space.setter
    def occupied_space(self, occupied_space: int) -> None:
        """Устанавливает объем занятой памяти на флеш накопителе."""
        if type(occupied_space) is not int:
            raise TypeError("Объем занятой памяти должен быть целым числом")
        if occupied_space < 0:
            raise ValueError("Объем занятой памяти не может быть отрицательным числом")
        self._occupied_space = occupied_space

    def is_empty_flash_drive(self) -> bool:
        """
        Функция которая проверяет является ли флеш накопитель пустым

        :return: True, если флеш накопитель пустой

        Примеры:
        >>> flash = FlashDrive(1024, 0)
        >>> flash.is_empty_flash_drive()
        True
        """
        if self.occupied_space:
            return False
        return True

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
        if file_size < 0 or file_size > (self.memory - self.occupied_space):
            raise ValueError("Объем добавляемого файла должен быть больше 0 и меньше свободного места"
                             "на флеш накопителе")
        self.occupied_space += file_size

    def clear_flash_drive(self) -> bool:
        """
        Очистка флеш накопителя.

        :return: True, если очистка флеш накопителя прошла успешно

        Примеры:
        >>> flash = FlashDrive(1024, 515)
        >>> flash.clear_flash_drive()
        True
        """
        self.occupied_space = 0
        if not self.is_empty_flash_drive:
            return False
        return True

    @staticmethod
    def more_free_memory(flash_drive_1, flash_drive_2):
        """
        >>> flash_1 = FlashDrive(1024, 515)
        >>> flash_2 = FlashDrive(1024, 256)
        >>> flash_2 == FlashDrive.more_free_memory(flash_1, flash_2)
        True
        """
        if type(flash_drive_1) is not FlashDrive or type(flash_drive_2) is not FlashDrive:
            raise TypeError("Передаваемые объекты должны быть типа FlashDrive")
        if flash_drive_1.memory - flash_drive_1.occupied_space < flash_drive_2.memory - flash_drive_2.occupied_space:
            return flash_drive_2
        return flash_drive_1


class Lamp:
    """
    Родительский объект "Лампа", в котором учитываются только световые характеристики.
    """

    def __init__(self, power: Union[int, float], light_flow: Optional = None):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param power: Мощность лампы, Вт
        :param light_flow: Световой поток, Лм

        Примеры:
        >>> lamp = Lamp(5, 500)
        """

        if not isinstance(power, (int, float)):
            raise TypeError("Мощность лампы должна быть int или float")
        if power < 0:
            raise ValueError("Мощность лампы должна быть типа положительным числом")
        self._power = power

        if light_flow is None:
            self._light_flow = None
        else:
            if not isinstance(light_flow, int):
                raise TypeError("Световой поток лампы должен быть int")
            if light_flow < 0:
                raise ValueError("Световой поток лампы должен быть больше 0")
            self._light_flow = light_flow

    @property
    def power(self):
        return self._power

    @property
    def light_flow(self):
        return self._light_flow

    def efficiency(self) -> int:
        """
        Функия, которая считает эффективность лампы.
        Лм / Вт

        :raise ValueError: Если параметр Световой поток (light_flow) не задан, то вызываем ошибку

        Примеры:
        >>> lamp = Lamp(10, 1000)
        >>> lamp.efficiency()
        100

        Traceback (most recent call last):
            ...
        ValueError: Параметр "Световой поток" не задан
        """
        if self.light_flow is None:
            raise ValueError('Параметр "Световой поток" не задан')
        return int(self.light_flow / self.power)

    def calculate_energy(self, hour: Union[int, float]) -> float:
        """
        Посчитать затраченную лампой энергию за кол-во часов

        :param hour: Время, которая лампа работала, ч

        :return: Возвращает затраченную лампой энергию за кол-во часов, кВт * ч

        Примеры:
        >>> lamp = Lamp(5)
        >>> lamp.calculate_energy(3)
        0.015
        """
        if not isinstance(hour, (int, float)):
            raise TypeError("Световой поток лампы должен быть int")
        return self.power * hour / 1000

    def __repr__(self) -> str:
        """
        Примеры:
        >>> lamp = Lamp(5, 300)
        >>> repr(lamp)
        'Lamp(5, 300)'
        """
        return f'{self.__class__.__name__}({self.power!r}, {self.light_flow!r})'


class LedLamp(Lamp):
    """
    Объект "Светодиодная лампа", в котором учитываются только световые характеристики.
    """
    def __init__(self, power: Union[int, float], color_temperature: int, light_flow: Optional = None):
        """
        Создание и подготовка к работе объекта "Светодиодная лампа"

        :param power: Мощность лампы, Вт
        :param color_temperature: Температура света лампы, К
        :param light_flow: Световой поток, Лм

        Примеры:
        >>> led_lamp = LedLamp(5, 4000, 500)
        """

        super().__init__(power, light_flow)

        if not isinstance(color_temperature, int):
            raise TypeError("Температура света лампы должна быть int")
        if color_temperature < 1500 or color_temperature > 7000:
            raise ValueError("Температура света лампы должна быть в диапазоне от 1500 до 7000 К")
        self.color_temperature = color_temperature

    def __repr__(self) -> str:
        """
        Примеры:
        >>> led_lamp = LedLamp(5, 4000, 300)
        >>> repr(led_lamp)
        'LedLamp(5, 4000, 300)'
        """
        return f'{self.__class__.__name__}({self.power!r}, {self.color_temperature!r}, {self.light_flow!r})'


class IncandescentLamp(Lamp):
    filament = "wolfram"

    @classmethod
    def change_filament(cls, filament: str) -> None:
        if not isinstance(filament, str):
            raise TypeError("Новая нить накала должна быть типа str ")
        cls.filament = filament


if __name__ == "__main__":
    import doctest
    doctest.testmod()
