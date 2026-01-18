#!/usr/bin/env python3

def count_days(day: int) -> None:
    """
    Recursively count down and print each day.

    Args:
        day (int): The current day number to print.
    """
    if day > 1:
        count_days(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    """
    Prompt the user for days until harvest and display a countdown.

    The function uses recursion to print each day leading up to harvest,
    then prints a final harvest message.
    """
    harvest_days = int(input("Days until harvest: "))
    if harvest_days > 0:
        count_days(harvest_days)
    print("Harvest time!")
