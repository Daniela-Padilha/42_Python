def ft_harvest_total():
    total:	int = 0
    day1:	int = 0
    day2:	int = 0
    day3:	int = 0

    print("Day 1 harvest: ", end="")
    day1 = int(input())
    print("Day 2 harvest: ", end="")
    day2 = int(input())
    print("Day 3 harvest: ", end="")
    day3 = int(input())
    total = day1 + day2 + day3
    print("Total harvest:", total)
