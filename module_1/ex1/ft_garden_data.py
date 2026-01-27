#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with a name, height, and age in days.
    """

    def __init__(
            self,
            name: str = "Iris",
            height: int = 10,
            days_old: int = 30
    ) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            days_old (int): Age of the plant in days.
        """
        self.name: str = name
        self.height: int = height
        self.days_old: int = days_old


if __name__ == "__main__":
    plants: list[Plant] = [
            Plant(),
            Plant("Rose", 25, 30),
            Plant("Cactus", 15, 120)
            ]
    print("=== Welcome to My Garden ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.days_old} days old")
