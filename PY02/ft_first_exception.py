def check_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if (temp < 0):
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None
    elif (temp > 40):
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")

    print("\nAll tests completed- program didn't crash!")


def main():
    test_temperature_input()
    print("\nNow test your own values")
    user_in: str = input("\nEnter temperature: ")
    check_temperature(user_in)


if __name__ == "__main__":
    main()
