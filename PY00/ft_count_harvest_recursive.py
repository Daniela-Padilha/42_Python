def ft_count_harvest_recursive(current: int = 1, total: int | None = None) -> None:
    if (total is None):
        print("total until harvest: ", end="")
        total = int(input())
    if (current > total):
        print("Harvest time!")
    else:
        print("Day", current)
        ft_count_harvest_recursive(current + 1, total)
