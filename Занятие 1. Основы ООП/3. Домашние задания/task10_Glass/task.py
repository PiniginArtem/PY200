class Glass:
    material = "glass"

    @classmethod
    def get_material(cls):
        return cls.material


if __name__ == "__main__":
    print(Glass.get_material())

