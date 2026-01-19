def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ):
    """
    Validate plant health parameters and report plant status.

    The function checks:
    - the validity of the plant name
    - that the water level is an integer between 1 and 10
    - that the sunlight hours are an integer between 2 and 12

    If any condition fails, a ValueError is raised.
    If all checks pass, the plant is considered healthy.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level (1–10).
        sunlight_hours (int): Daily sunlight hours (2–12).

    Raises:
        ValueError: If any validation rule is violated.
    """
    if plant_name is None or plant_name == "" or type(plant_name) is not str:
        raise ValueError("invalide Plant Name")
    elif type(water_level) is not int:
        raise ValueError("Watter Level isn't an integer")
    elif water_level > 10 or water_level < 1:
        raise ValueError("Watter Level must be between 1 and 10")
    elif type(sunlight_hours) is not int:
        raise ValueError("Sunlight Hours isn't an integer")
    elif sunlight_hours > 12 or sunlight_hours < 2:
        raise ValueError("Sunlight Hours must be between 2 and 12")
    else:
        print(f"{plant_name} is healthy")


def test_plant_checks():
    """
    Test the plant health checker with valid and invalid inputs.
    """
    print("=== Test 1: Valid plant data ===")
    try:
        check_plant_health("Tomato", 5, 6)
    except ValueError as error:
        print(f"Error: {error}")

    print("\n=== Test 2: Invalid plant name ===")
    try:
        check_plant_health("", 5, 6)
    except ValueError as error:
        print(f"Caught error: {error}")

    print("\n=== Test 3: Invalid water level ===")
    try:
        check_plant_health("Rose", 0, 6)
    except ValueError as error:
        print(f"Caught error: {error}")

    print("\n=== Test 4: Invalid sunlight hours ===")
    try:
        check_plant_health("Sunflower", 5, 15)
    except ValueError as error:
        print(f"Caught error: {error}")


if __name__ == "__main__":
    test_plant_checks()
