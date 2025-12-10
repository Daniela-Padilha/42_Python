#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def message(self) -> None:
        print(self.name, ":", end=" ", sep="")
        print(self.height, "cm,", end=" ", sep="")
        print(self.age, "days old")


def ft_garden_data() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.message()
    sunflower.message()
    cactus.message()


if (__name__ == "__main__"):
    ft_garden_data()
