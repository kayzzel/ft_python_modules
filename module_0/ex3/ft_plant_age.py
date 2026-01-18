#!/usr/bin/env python3

def ft_plant_age() -> None:
    """
    Prompt the user for a plant's age and determine harvest readiness.

    If the plant is older than 60 days, the function indicates that it is
    ready to harvest; otherwise, it reports that the plant needs more time
    to grow.
    """
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
