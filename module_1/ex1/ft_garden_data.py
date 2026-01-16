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
    plant: Plant = Plant()
    print(f"""
=== Welcome to My Garden ===
Plant: {plant.name}
Height: {plant.height}cm
Age: {plant.days_old} days
=== End of Program ===
          """)
