class GardenError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "The tomato plant is wilting!"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Not enough water in the tank!"):
        super().__init__(msg)


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    for error in (PlantError(), WaterError()):
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
