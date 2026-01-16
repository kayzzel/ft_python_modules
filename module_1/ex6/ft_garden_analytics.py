class Plant:
    """
    Represents a plant with a name, height, and age in days.
    """

    def __init__(
            self,
            name: str = "Iris",
            height: int = 10,
            days_old: int = 30,
            status: str = "Plant"
    ) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            days_old (int): Age of the plant in days.
        """
        self.name: str = name
        self._height: int = height
        self._days_old: int = days_old
        self._status: str = status

    def age(self) -> None:
        """
        Increase the age of the plant by one day.
        """
        self._days_old += 1

    def grow(self) -> None:
        """
        Increase the height of the plant by one centimeter.
        """
        self._height += 1

    def set_height(self, height: int) -> None:
        """
        Set the height of the plant with validation.

        Rejects non-integer and negative values and prints a security message
        when an invalid operation is attempted.

        Args:
            height (int): New height of the plant in centimeters.
        """
        if (type(height) is not int):
            print("""
Invalid operation attempted: height {height}cm [REJECTED]
Security: Non Interger height rejected
                  """)
        elif (height < 0):
            print("""
Invalid operation attempted: height {height}cm [REJECTED]
Security: Negative height rejected
                  """)
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_status(self, status: str) -> None:
        if (type(status) is not str):
            print("""
Invalid operation attempted: status -> {status} [REJECTED]
Security: Non String status rejected
                  """)
        elif (status != "Plant" and status != "FloweringPlant"
                and status != "PrizeFlower"):
            print("""
Invalid operation attempted: status -> {status} [REJECTED]
Security: Non vvalid status value rejected
                  """)
        else:
            self._status = status
            print(f"Status updated: {self._status} [OK]")

    def set_age(self, age: int) -> None:
        """
        Set the age of the plant with validation.

        Rejects non-integer and negative values and prints a security message
        when an invalid operation is attempted.

        Args:
            age (int): New age of the plant in days.
        """
        if (type(age) is not int):
            print("""
Invalid operation attempted: age {age} days [REJECTED]
Security: Non Interger age rejected
                  """)
        elif (age < 0):
            print("""
Invalid operation attempted: age {age}cm [REJECTED]
Security: Negative age rejected
                  """)
        else:
            self._days_old = age
            print(f"Height updated: {self._days_old} days [OK]")

    def get_status(self) -> str:
        return self._status

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            int: Height of the plant in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            int: Age of the plant in days.
        """
        return self._days_old

    def get_info(self) -> None:
        """
        Print the plant's name, height, and age.
        """
        print(f"{self.name} : {self._height}cm, {self._days_old} days old")


class Flower(Plant):
    """
    Represents a flowering plant with a color and blooming behavior.
    """

    def __init__(
            self,
            name: str = "Iris",
            height: int = 10,
            days_old: int = 30,
            status: str = "Plant",
            color: str = "purple"
            ) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height of the flower in centimeters.
            days_old (int): Age of the flower in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, days_old)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        """
        Trigger the blooming process of the flower.

        Prints a message indicating whether the flower is blooming
        or has already bloomed.
        """
        if not self.bloomed:
            print(f"{self.name} is blooming beautifully!")
            self.bloomed = True
        else:
            print(f"{self.name} already bloomed")

    def get_info(self) -> None:
        """
        Print detailed information about the flower.
        """
        print(f"{self.name} (Flower): {self._height}cm, "
              f"{self._days_old} days old, color : {self.color}")


class Tree(Plant):
    """
    Represents a tree with a trunk diameter and shade-producing capability.
    """

    def __init__(
            self,
            name: str = "Oak",
            height: int = 500,
            days_old: int = 365,
            status: str = "Plant",
            trunk_diameter: int = 50
            ) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height of the tree in centimeters.
            days_old (int): Age of the tree in days.
            trunk_diameter (int): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, days_old, status)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and display the shade area produced by the tree.
        """
        shade_area: float = self._height // 2 * self.trunk_diameter * 7 / 10000
        print(f"{self.name} provides {round(shade_area, 2)} "
              f"square meters of shade")

    def get_info(self) -> None:
        """
        Print detailed information about the tree.
        """
        print(f"{self.name} (Tree): {self._height}cm, "
              f"{self._days_old} days old, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant with harvest and nutritional information.
    """

    def __init__(
            self,
            name: str = "Tomato",
            height: int = 80,
            days_old: int = 90,
            status: str = "Plant",
            harvest_season: str = "summer",
            nutritional_value: str = "vitamine C"
            ) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height of the vegetable in centimeters.
            days_old (int): Age of the vegetable in days.
            harvest_season (str): Season in which the vegetable is harvested.
            nutritional_value (str): Main nutritional benefit of the vegetable.
        """
        super().__init__(name, height, days_old, status)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        """
        Print detailed information about the vegetable.
        """
        print(f"{self.name} (Vegetable): {self._height}cm, "
              f"{self._days_old} days old, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


class Garden:
    def __init__(
            self,
            owner: str,
            name: str,
            plants: list[Plant | Flower | Tree | Vegetable] = []
            ):
        self.owner: str = owner
        self.name: str = name
        self._plants: list[Plant | Flower | Tree | Vegetable] = plants
        self._total_growth = 0

    def add_plant(self, plant: Plant | Flower | Tree | Vegetable):
        self._plants = self._plants + [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    def garden_growth(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()
            self._total_growth += 1
            print(f"{plant.name} grew 1 cm")

    def height_validation(self):
        total_height: int = 0

        for plant in self._plants:
            if type(plant) is Tree:
                total_height += plant.get_height() / 5
            elif type(plant) is Vegetable:
                total_height += plant.get_height() * 2
            else:
                total_height += plant.get_height()
        if (total_height / len(self._plants) > 30):
            print("Height validation test: True")
        else:
            print("Height validation test: False")

    def garden_score(self):
        pass

    def get_plants(self) -> list[Plant | Flower | Tree | Vegetable]:
        return self._plants

    def get_total_growth(self) -> int:
        return self._total_growth


class GardenManager:
    def __init__(
            self,
            gardens: dict[str, Garden] = {}
            ):
        self._gardens: dict[str, Garden] = gardens

    class GardenStats:
        @staticmethod
        def display_garden_stats(garden: Garden):
            plants_status: dict[str, int] = {
                    "Plant": 0,
                    "FloweringPlant": 0,
                    "PrizeFlower": 0
                    }
            plants: list[Plant | Flower | Tree | Vegetable] = \
                garden.get_plants()
            print(f"==== {garden.name} Report ====")
            print("Plants in garden:")
            for plant in plants:
                print(f"- {plant.name}: {plant.get_height()}", end="")
                if type(plant) is Flower:
                    print(f", {plant.color} flowers)", end="")
                if plant.get_status() == 'FloweringPlant':
                    print(" (blooming)", end="")
                if plant.get_status() == 'PrizeFlower':
                    print(" (blooming), Prize points: 10", end="")
                plants_status[plant.get_status()] += 2
                print("")

            print(f"\nPlants added: {len(plants)}, \
Total growth: {garden.get_total_growth()}cm")

            print(f"Plant Type: \
{plants_status['Plant']} Regular, \
{plants_status['FloweringPlant']} Flowering, \
{plants_status['PrizeFlower']} Prize flower")

    def add_garden(self, garden: Garden):
        if (type(garden) is not Garden):
            print("""
Invalid operation attempted: Add Garden [REJECTED]
Security: Non Garden type Garden rejected
                  """)
        if (garden.name in self._gardens):
            print("""
Invalid operation attempted: Add Garden [REJECTED]
Security: Garden name already exist in GardenManager
                  """)
        else:
            self._gardens[garden.name] = garden

    def get_gardens(self):
        return self._gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===", end="\n\n")
    garden_manager: GardenManager = GardenManager(
            {"Alice's Garden": Garden("Alice's Garden", "Alice"),
             "Theo's Garden": Garden("Theo's Garden", "Theo")})
    garden_manager._gardens["Alice's Garden"].add_plant(
            Tree("Oak", 100, 150, "Plant", 20))
    garden_manager._gardens["Alice's Garden"].add_plant(
            Flower("Rose", 21, 30, "Plant", "red"))
    garden_manager._gardens["Alice's Garden"].add_plant(
            Flower("Sunflower", 50, 25, "Plant", "yellow"))
    print()
    garden_manager._gardens["Alice's Garden"].garden_growth()

    print()
    garden_manager.GardenStats.display_garden_stats(
            garden_manager._gardens["Alice's Garden"])

    print()
    garden_manager._gardens["Alice's Garden"].height_validation()
    print(f"Total Garden managed: {len(garden_manager.get_gardens())}")
