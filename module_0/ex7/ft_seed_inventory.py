#!/usr/bin/env python3

def ft_seed_inventory(seed: str, nbr: int, unit: str) -> None:
    """
    Display seed inventory information based on the specified unit.

    Depending on the unit provided, the function prints the quantity
    of seeds available as packets, grams, or area coverage.

    Args:
        seed (str): Name of the seed.
        nbr (int): Quantity of the seed.
        unit (str): Unit of measurement ("packets", "grams", or "area").
    """
    if unit == "packets":
        print(f"{seed.capitalize()} seeds: {nbr} packets available")
    elif unit == "grams":
        print(f"{seed.capitalize()} seeds: {nbr} grams total")
    elif unit == "area":
        print(f"{seed.capitalize()} seeds: covers {nbr} square meters")
    else:
        print("Unknown unit type")
