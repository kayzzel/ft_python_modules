#!/usr/bin/env python3

def ft_garden_summary() -> None:
    """
    Prompt the user for garden details and display a summary.

    The function asks for the garden name and the number of plants,
    then prints a short status summary indicating that the garden
    is growing well.
    """
    garden_name = input("Enter garden name: ")
    plant_nbr = input("Enter number of plants: ")
    print(f"Garden: {garden_name}\nPlants: {plant_nbr}\nStatus: Growing well!")
