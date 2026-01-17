#!/usr/bin/env python3

def count_days(day: int) -> None:
    if day > 1:
        count_days(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    harvest_days = int(input("Days until harvest: "))
    if (harvest_days > 0):
        count_days(harvest_days)
    print("Harvest time!")
