#!/usr/bin/env python3

def ft_count_harvest_recursive() -> None:
    """
    Prompt the user for days until harvest and display a countdown.

    The function uses recursion to print each day leading up to harvest,
    then prints a final harvest message.
    """
    def day_count_recursive(day: int):
        if day > 1:
            day_count_recursive(day - 1)
        print(f"Day {day}")

    day = int(input("Days until harvest: "))
    if day > 0:
        day_count_recursive(day)
    print("Harvest time!")
