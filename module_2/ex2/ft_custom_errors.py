#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base exception class for garden-related errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the GardenError with a custom message.

        Args:
            message (str): Description of the error.
        """
        super().__init__(message)


class PlantError(GardenError):
    """
    Exception raised for plant-specific errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the PlantError with a custom message.

        Args:
            message (str): Description of the plant error.
        """
        super().__init__(message)


class WatterError(GardenError):
    """
    Exception raised for watering-related errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the WatterError with a custom message.

        Args:
            message (str): Description of the watering error.
        """
        super().__init__(message)


def plant_watter(plant_name: str, watter: int) -> None:
    """
    Check if a plant is wilting based on water level.

    Raises:
        PlantError: If the water level is non-negative (plant is wilting).
    """
    if watter >= 0:
        raise PlantError(f"The {plant_name} plant is wilting!")


def watter_tank(watter: int) -> None:
    """
    Check if the water tank has sufficient water.

    Raises:
        WatterError: If the water amount is below 10 units.
    """
    if watter < 10:
        raise WatterError("Not enough watter in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing Plant Error...")
    try:
        plant_watter("tomato", 0)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()
    print("Testing Watter Error...")
    try:
        watter_tank(0)
    except WatterError as error:
        print(f"Caught Watter Error: {error}")

    print()
    print("Testing All Error...")
    try:
        plant_watter("tomato", 0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        watter_tank(0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print()
    print("All custom error types work correctly!")
