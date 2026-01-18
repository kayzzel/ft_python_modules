#!/usr/bin/env python3

def ft_harvest_total() -> None:
    """
    Prompt the user for harvest amounts over three days and display the total.

    The function asks for integer harvest values for three consecutive days,
    calculates their sum, and prints the total harvest.
    """
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day1 + day2 + day3}")
