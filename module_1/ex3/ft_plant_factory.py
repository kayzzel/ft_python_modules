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

    def age(self) -> None:
        """
        Increase the age of the plant by one day.
        """
        self.days_old += 1

    def grow(self) -> None:
        """
        Increase the height of the plant by one centimeter.
        """
        self.height += 1

    def get_info(self) -> None:
        """
        Print the plant's name, height, and age.
        """
        print(f"{self.name} : {self.height}cm, {self.days_old} days old")


class Factory:
    """
    Factory class responsible for creating and tracking Plant objects.
    """

    def __init__(self) -> None:
        """
        Initialize the Factory with an empty garden and a plant counter.
        """
        self.garden: list[Plant] = []
        self.plant_count = 0

    def create_plant(self, name: str, height: int, age: int) -> None:
        """
        Create a new Plant and add it to the garden.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.garden = self.garden + [Plant(name, height, age)]
        self.plant_count += 1
        print(f"Created: {name} ({height}cm, {age} days)")

    def __str__(self) -> str:
        """
        Return a human-readable summary of the factory's production.

        Returns:
            str: Total number of plants created.
        """
        return "Total Plant Created: " + str(self.plant_count)


if __name__ == "__main__":
    factory: Factory = Factory()
    factory.create_plant("Rose", 25, 30)
    factory.create_plant("Oak", 200, 365)
    factory.create_plant("Cactus", 5, 90)
    factory.create_plant("Sunflower", 80, 45)
    factory.create_plant("Fern", 15, 120)
    print(f"\n{factory}")
