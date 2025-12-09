def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(seed_type.capitalize(), "seeds:", quantity, unit, "available")
        return
    if (unit == "grams"):
        print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
        return
    if (unit == "area"):
        print(seed_type.capitalize(), "seeds: covers", quantity,
              "square meters")
        return
    else:
        print("Unknown unit type")
