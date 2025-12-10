#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(self.name, ":", end=" ", sep="")
        print(self.height, "cm,", end=" ", sep="")
        print(self.age, "days old")

    def grow(self) -> None:
        i: int = 7
        while (i > 1):
            self.height += 1
            i -= 1

    def ageing(self) -> None:
        i: int = 7
        while (i > 1):
            self.age += 1
            i -= 1


def ft_plant_growth() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    print("=== Day 7 ===")
    for plant in plants:
        plant.ageing()
        plant.grow()
        plant.get_info()
    print("Growth this week: +6cm", sep="")


if (__name__ == "__main__"):
    ft_plant_growth()
