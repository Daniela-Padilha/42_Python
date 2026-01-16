#! usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str):
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print("=== Garden Security System ===")
        print(f"Plant created: {name}")
    
    def get_info(self) -> None:
        print(
            f"Current plant: {self.name} "
            f"({self.__height}cm, {self.__age} days)"
        )

    def set_height(self, height: int) -> None:
        if (height >= 0):
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


def ft_garden_security() -> None:
    Rose: SecurePlant = SecurePlant("Rose")
    Rose.set_height(25)
    Rose.set_age(30)
    print("\n")
    Rose.set_height(-5)
    print("\n")
    Rose.get_info()


if __name__ == "__main__":
    ft_garden_security()