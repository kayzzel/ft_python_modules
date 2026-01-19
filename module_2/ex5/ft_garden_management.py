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


class WaterError(GardenError):
    """
    Exception raised for watering-related errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the WaterError with a custom message.

        Args:
            message (str): Description of the watering error.
        """
        super().__init__(message)


class SunError(GardenError):
    """
    Exception raised for sunlight-related errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the SunError with a custom message.

        Args:
            message (str): Description of the sunlight error.
        """
        super().__init__(message)


class Plant:
    """
    Represents a plant with name, water level, and sunlight hours.

    The class validates all inputs using properties and raises custom errors.
    """

    def __init__(self, name: str, water: int = 8, sun: int = 8) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            water (int): Water level (1-10).
            sun (int): Sunlight hours (2-12).
        """
        self.name: str = name
        self.water: int = water
        self.sun: int = sun

    @property
    def name(self) -> str:
        """
        Get the plant name.

        Returns:
            str: Name of the plant.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Set the plant name with validation.

        Raises:
            PlantError: If the name is empty, None, or not a string.
        """
        if name is None or name == "" or type(name) is not str:
            raise PlantError("invalide Plant Name")
        else:
            self.__name: str = name

    @property
    def water(self) -> int:
        """
        Get the water level.

        Returns:
            int: Water level of the plant.
        """
        return self.__water

    @water.setter
    def water(self, water: int) -> None:
        """
        Set the water level with validation.

        Raises:
            WaterError: If water is not an integer or outside 1-10.
        """
        if type(water) is not int:
            raise WaterError("Water Level isn't an integer")
        elif water > 10 or water < 1:
            raise WaterError("Water Level must be between 1 and 10")
        else:
            self.__water: int = water

    @property
    def sun(self) -> int:
        """
        Get the sunlight hours.

        Returns:
            int: Sunlight hours of the plant.
        """
        return self.__sun

    @sun.setter
    def sun(self, sun: int) -> None:
        """
        Set the sunlight hours with validation.

        Raises:
            SunError: If sun is not an integer or outside 2-12.
        """
        if type(sun) is not int:
            raise SunError("Sun isn't an integer")
        elif sun > 12 or sun < 2:
            raise SunError("Sun must be between 2 and 12")
        else:
            self.__sun: int = sun

    def add_water(self) -> None:
        """
        Increase the plant's water level by 1.
        """
        self.__water += 1

    def add_sun(self) -> None:
        """
        Increase the plant's sunlight hours by 1.
        """
        self.__sun += 1

    def check_plant_health(self) -> None:
        """
        Validate plant health parameters and report plant status.

        This method checks the plant name, water level, and sunlight hours.
        If any validation fails, the appropriate GardenError is raised.

        Raises:
            PlantError: If plant name is invalid.
            WaterError: If water level is invalid.
            SunError: If sunlight hours are invalid.
        """
        if self.name is None or self.name == "" or type(self.name) is not str:
            raise PlantError("invalide Plant Name")
        elif type(self.water) is not int:
            raise WaterError("Watter Level isn't an integer")
        elif self.water > 10 or self.water < 1:
            raise WaterError("Watter Level must be between 1 and 10")
        elif type(self.sun) is not int:
            raise SunError("Sunlight Hours isn't an integer")
        elif self.sun > 12 or self.sun < 2:
            raise SunError("Sunlight Hours must be between 2 and 12")
        else:
            print(f"{self.name}: healthy (water: {self.water}, sun: self.sun)")


class GardenManager:
    """
    Manages a collection of Plant objects and handles watering operations.
    """

    def __init__(self) -> None:
        """
        Initialize the GardenManager with an empty plant list and water tank.
        """
        self.__plants: list[Plant] = []
        self.water_tank: int = 100

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """
        Create and add a plant to the garden.

        If any validation fails, the error is printed instead.

        Args:
            name (str): Name of the plant.
            water (int): Water level (1-10).
            sun (int): Sunlight hours (2-12).
        """
        try:
            plant: Plant = Plant(name, water, sun)
        except GardenError as err:
            print(f"Error adding Plant: {err}")
        else:
            self.__plants += [plant]
            print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Water all plants in the garden.

        Decreases the water tank by 1 per plant.
        Raises a WaterError if tank is empty.
        """
        print("Opening watering system")
        try:
            for plant in self.__plants:
                if self.water_tank < 1:
                    raise WaterError("not enought water in tank")
                self.water_tank -= 1
                plant.add_water()
                print(f"Watering {plant.name} - success")
        except GardenError as err:
            print(f"Watering {plant.name} error: {err}")
        finally:
            print("Closing watering system (cleanup)")

    def check_garden_heath(self) -> None:
        """
        Check health of all plants in the garden.

        Prints an error message if any plant health check fails.
        """
        for plant in self.__plants:
            try:
                plant.check_plant_health()
            except GardenError as err:
                print(f"Error checking {plant.name}: {err}")

    def get_plants(self) -> list[Plant]:
        """
        Return the list of plants in the garden.

        Returns:
            list[Plant]: All plants managed by this GardenManager.
        """
        return self.__plants


def test_garden_manager() -> None:
    garden = GardenManager()
    print("=== Garden Management System ===")

    print()
    print("Adding plants to garden...")
    garden.add_plant("tomato", 4, 8)
    garden.add_plant("lettuce", 2, 12)
    garden.add_plant("", 8, 8)

    print()
    print("Watering plants...")
    garden.water_plants()

    print()
    garden.get_plants()[1].add_sun()
    print("Checking plant health...")
    garden.check_garden_heath()

    print()
    print("Testing error recovery...")
    garden.water_tank = 0
    garden.water_plants()
    print("System recovered and continuing...")


if __name__ == "__main__":
    test_garden_manager()
