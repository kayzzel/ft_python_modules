#!/usr/bin/env python3

def ft_water_reminder() -> None:
    """
    Prompt the user for the number of days since last watering and
    display a watering reminder if needed.

    If more than two days have passed since the last watering,
    the function advises watering the plants; otherwise, it reports
    that the plants are fine.
    """
    last_watering = int(input("Days since last watering: "))
    print("Water the plants!" if (last_watering > 2) else "Plants are fine")
