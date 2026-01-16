#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.oldHeight: int = 0

    def get_info(self) -> None:
        print(f"{self.name}: {self.height:.0f}cm, {self.age} days old")

    def grow(self) -> None:
        self.oldHeight = self.height
        i: int = 7
        while (i > 1):
            self.height += 1
            i -= 1

    def ageing(self) -> None:
        i: int = 7
        while (i > 1):
            self.age += 1
            i -= 1

    def get_growth(self) -> None:
        res: int = self.height - self.oldHeight
        print("Growth this week: ", "+", res, "cm", sep="")


def ft_plant_factory() -> None:
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    # arg unpacking and list comprehension
    garden: list[Plant] = [Plant(*p) for p in data]
    total: int = 0

    print("=== Plant Factory Output ===")
    for plant in garden:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        total += 1
    print(f"\nTotal plants created: {total}")


if __name__ == "__main__":
    ft_plant_factory()
