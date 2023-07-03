from typing import Union, Optional


class LedLamp:
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
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность лампы должна быть int или float")
        if power < 0:
            raise ValueError("Мощность лампы должна быть типа положительным числом")
        self.power = power

        if not isinstance(color_temperature, int):
            raise TypeError("Температура света лампы должна быть int")
        if color_temperature < 1500 or color_temperature > 7000:
            raise ValueError("Температура света лампы должна быть в диапазоне от 1500 до 7000 К")
        self.color_temperature = color_temperature

        if light_flow is None:
            self.light_flow = None
        else:
            if not isinstance(light_flow, int):
                raise TypeError("Световой поток лампы должен быть int")
            if light_flow < 0:
                raise ValueError("Световой поток лампы должен быть больше 0")
            self.light_flow = light_flow

    def efficiency(self) -> int:
        """
        Функия, которая считает эффективность лампы.
        Лм / Вт * 100%

        :raise ValueError: Если параметр Световой поток (light_flow) не задан, то вызываем ошибку

        Примеры:
        >>> led_lamp = LedLamp(5, 4000)
        >>> led_lamp.efficiency()
        Traceback (most recent call last):
            ...
        ValueError: Параметр "Световой поток" не задан
        """
        if self.light_flow is None:
            raise ValueError('Параметр "Световой поток" не задан')
        ...

    def calculate_energy(self, hour: Union[int, float]) -> float:
        """
        Посчитать затраченную лампой энергию за кол-во часов

        :param hour: Время, которая лампа работала, ч

        :return: Возвращает затраченную лампой энергию за кол-во часов, кВт * ч

        Примеры:
        >>> led_lamp = LedLamp(5, 4000, 300)
        >>> led_lamp.calculate_energy(3)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
