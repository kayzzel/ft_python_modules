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


def grow_n_days(plant: Plant, n: int = 7) -> None:
    """
    Simulate the growth of a plant over a given number of days.

    Each day, the plant grows by one centimeter and ages by one day.

    Args:
        plant (Plant): The plant to grow.
        n (int): Number of days to simulate.
    """
    base_height: int = plant.height
    print("==== days 0 ====")
    plant.get_info()

    for _ in range(n):
        plant.grow()
        plant.age()

    print(f"==== days {n} ====")
    plant.get_info()
    print(f"Growth during {n} days: +{plant.height - base_height}cm")


if __name__ == "__main__":
    plant: Plant = Plant()
    grow_n_days(plant)
