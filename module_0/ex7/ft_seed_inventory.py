#!/usr/bin/env python3

def ft_seed_inventory(seed: str, nbr: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed} seeds: {nbr} packets available")
    elif (unit == "grams"):
        print(f"{seed} seeds: {nbr} grams total")
    elif (unit == "area"):
        print(f"{seed} seeds: covers {nbr} square meters")
    else:
        print("Wrong unit!")
