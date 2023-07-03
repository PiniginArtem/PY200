from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, water: Union[int, float]):
        if not isinstance(water, (int, float)):
            raise TypeError
        if water < 0 or self.capacity_volume - self.occupied_volume < water:
            raise ValueError
        self.occupied_volume += water

    def remove_water(self, water: Union[int, float]):
        if not isinstance(water, (int, float)):
            raise TypeError
        if water < 0 or self.occupied_volume < water:
            raise ValueError
        self.occupied_volume -= water


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    glass.add_water(50)
    print(glass.occupied_volume)
    glass.remove_water(200)
