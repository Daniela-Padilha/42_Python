def ft_plant_age():
    age: int = 0

    print("Enter plant age in days: ", end="")
    age = int(input())
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
