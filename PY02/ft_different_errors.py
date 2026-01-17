def garden_operations() -> None:
    value: int = int("abc")
    nbr: int = 1/0
    file = open("noexist.txt")
    fruit = {"name": "apple", "color": "red"}
    print(fruit["price"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionError...")
    try:
        1/0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        fruit = {"name": "apple", "color": "red"}
        print(fruit["price"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def main():
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
