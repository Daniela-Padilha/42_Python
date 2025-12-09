def ft_count_harvest_iterative() -> None:
    days: int = 0

    print("Days until harvest: ", end="")
    days = int(input()) + 1
    for i in range(1, days):
        print("Day", i)
    print("Harvest time!")
