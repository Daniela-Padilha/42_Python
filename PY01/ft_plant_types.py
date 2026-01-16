class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()} ({self.__class__.__name__}): "
            f"{self.height:.0f}cm, {self.age} days" + self.extra_info()
        )

    def extra_info(self) -> str:
        return ""

    def special_method(self) -> None:
        print("This plant does nothing special")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")

    def extra_info(self) -> str:
        return f", {self.color} color"

    def special_method(self):
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade: int = self.trunk_diameter + (self.trunk_diameter / 2)
        print(
          f"{self.name.capitalize()} provides {shade} square meters of shade"
        )

    def extra_info(self) -> str:
        return f", {self.trunk_diameter}cm diameter"

    def special_method(self):
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season

    def nutritional_value(self) -> None:
        print(
             f"{self.name.capitalize()} is rich in vitamin C"
        )

    def extra_info(self) -> str:
        return f", {self.harvest_season} harvest"

    def special_method(self):
        self.nutritional_value()


def ft_plant_types() -> None:
    print(
         "=== Garden Plant Types ===\n"
    )
    garden: list[Plant] = [
        Flower("rose", 25, 30, "red"),
        Flower("Tulip", 10, 5, "blue"),
        Tree("oak", 500, 1825, 50),
        Tree("Pine", 1000, 2000, 200),
        Vegetable("tomato", 80, 90, "summer"),
        Vegetable("pumpkin", 100, 60, "autumn")
    ]
    for plant in garden:
        plant.get_info()
        plant.special_method()
        print("\n")


if __name__ == "__main__":
    ft_plant_types()
