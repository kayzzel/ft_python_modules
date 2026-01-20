#!/usr/bin/env python3

def ft_count_harvest_recursive(day: int = -1) -> None:
    """
    Prompt the user for days until harvest and display a countdown.

    The function uses recursion to print each day leading up to harvest,
    then prints a final harvest message.
    """
    if (day == -1):
        day = int(input("Days until harvest: "))
    if day > 0:
        print(f"Day {day}")
        ft_count_harvest_recursive(day - 1)
    if day == 0:
        print("Harvest time!")
