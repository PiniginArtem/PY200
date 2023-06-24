from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume  # объём стакана
        self.occupied_volume = occupied_volume  # заполненный объём


if __name__ == "__main__":
    glass_1 = Glass(12, 3)
    glass_2 = Glass(5.5, 2.1)

    glass_3 = Glass("abc", [1, 2])
    print(glass_3.occupied_volume)
