#!/usr/bin/env python3

def ft_count_harvest_iterative() -> None:
    """
    Prompt the user for days until harvest and display an iterative countdown.

    The function prints each day from day 1 up to the harvest day,
    then prints a final harvest message.
    """
    harvest_days = int(input("Days until harvest: "))
    for day in range(1, harvest_days + 1):
        print(f"Day {day}")
    print("Harvest time!")
