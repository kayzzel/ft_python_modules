class WatteringError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if plant is None:
                raise WatteringError("Plant name isn't define")
            elif type(plant) is not str:
                raise WatteringError("Plant name is not a string")
            elif plant == "":
                raise WatteringError("Plant name is empty")
            else:
                print(f"Watering {plant}")
    except WatteringError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Test the watering system with valid and invalid plant lists.
    Demonstrates that cleanup always happens.
    """
    print("=== Test 1: Normal watering ===")
    good_plants: list[str] = ["Rose", "Tomato", "Sunflower"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\n=== Test 2: Watering with an error ===")
    bad_plants: list[str] = ["Rose", 42, "Sunflower"]
    water_plants(bad_plants)


if __name__ == "__main__":
    test_watering_system()
