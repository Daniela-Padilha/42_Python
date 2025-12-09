def ft_water_reminder() -> None:
    days: int = 0

    print("Days since last watering: ", end="")
    days = int(input())
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
