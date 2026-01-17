#!/usr/bin/env python3

def ft_water_reminder() -> None:
    last_watering = int(input("Days since last watering: "))
    print("Water the plants!" if (last_watering > 2) else "Plants are fine")
