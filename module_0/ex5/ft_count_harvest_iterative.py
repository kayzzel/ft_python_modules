#!/usr/bin/env python3

def ft_count_harvest_iterative() -> None:
    harvest_days = int(input("Days until harvest: "))
    for day in range(1, harvest_days + 1):
        print(f"Day {day}")
    print("Harvest time!")
