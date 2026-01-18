#!/usr/bin/env python3

def ft_plot_area() -> None:
    """
    Prompt the user for plot dimensions and display the calculated area.

    The user is asked to enter the length and width as integers.
    The function then computes and prints the plot area.
    """
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
