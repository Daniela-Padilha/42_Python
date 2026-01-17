# Parent class
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name.capitalize()
        self.height: int = height
        self.age: int = age

    def grow(self, cm: int) -> int:
        self.height += cm
        print(
            f"{self.name} grew {cm}cm"
        )
        return cm

    def get_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm" + self.extra_info()
        )

    def extra_info(self) -> str:
        return ""


# Child class
class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def extra_info(self) -> str:
        return f", {self.color} flowers (blooming)"


# Grandchild class
class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int):
        super().__init__(name, height, age, color)
        self.points: int = points

    def extra_info(self) -> str:
        return (
             f", {self.color} flowers (blooming), "
             f"Prize points: {self.points}"
        )


# Utility class
class GardenManager:
    __gardens = []

    def __init__(self, garden_name: str, plants: list[Plant],
                 garden_score: int):
        self.garden_name: str = garden_name.capitalize()
        self.plants: list[Plant] = plants
        self.garden_score: int = garden_score
        self.total_growth: int = 0
        for plant in self.plants:
            print(
                f"Added {plant.name} to"
                f" {self.garden_name}'s garden"
            )
        GardenManager.__gardens.append(self)

    def grow_plants(self, cm: int) -> None:
        print(
                f"\n{self.garden_name} is helping all plants grow..."
            )
        if not self.plants:
            print(
                "There are no plants in this garden yet\n"
            )
        for plant in self.plants:
            self.total_growth += plant.grow(cm)
            if (isinstance(plant, PrizeFlower)):
                self.garden_score += plant.points

    def garden_report(self) -> None:
        self.stats = self.GardenStats(self)
        self.stats.list_plants()
        self.stats.plant_summary()
        self.stats.height_validation(self.plants)

    @classmethod
    def create_garden_network(cls):
        parts = []

        for garden in cls.__gardens:
            parts.append(f"{garden.garden_name}: {garden.garden_score}")
        line: str = ", ".join(parts)
        print(
            f"Garden scores - {line}"
        )
        total: int = len(cls.__gardens)
        print(
            f"Total gardens managed: {total}"
        )

    # Nested class
    class GardenStats:
        def __init__(self, manager):
            self.manager: GardenManager = manager
            self.num_plants: int = len(self.manager.plants)
            print(
                f"\n== {self.manager.garden_name}'s Garden Report ===\n"
            )

        def list_plants(self) -> None:
            print(
                "Plants in garden:"
            )
            for plant in self.manager.plants:
                plant.get_info()

        def plant_summary(self) -> None:
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            print(
                f"\nPlants added: {self.num_plants},"
                f" Total growth: {self.manager.total_growth}cm"
            )
            for plant in self.manager.plants:
                if (isinstance(plant, PrizeFlower)):
                    prize += 1
                elif (isinstance(plant, FloweringPlant)):
                    flowering += 1
                elif (isinstance(plant, Plant)):
                    regular += 1
            print(
                f"Plant types: {regular} regular, {flowering} flowering,"
                f" {prize} prize flowers"
            )

        @staticmethod
        def height_validation(plants: list[Plant]) -> None:
            val: bool = all(plant.height > 0 for plant in plants)
            print(
                f"\nHeight validation test: {val}"
            )


# main program
def ft_garden_analytics() -> None:
    print(
        "== Garden Management System Demo ===\n"
    )
    alice_plants: list[Plant] = [
        Plant("oak tree", 100, 1),
        FloweringPlant("rose", 25, 3, "red"),
        PrizeFlower("sunflower", 50, 5, "yellow", 10)
    ]
    bob_plants: list[Plant] = []
    alice_garden: GardenManager = GardenManager("Alice", alice_plants, 208)
    bob_garden: GardenManager = GardenManager("Bob", bob_plants, 92)
    alice_garden.grow_plants(1)
    alice_garden.garden_report()
    bob_garden.grow_plants(2)
    GardenManager.create_garden_network()


if __name__ == "__main__":
    ft_garden_analytics()
