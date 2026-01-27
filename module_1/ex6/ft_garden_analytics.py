#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with a name, height, age, and status.
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
            status (str): Classification status of the plant.
        """
        self.name: str = name
        self.__height: int = height
        self.__days_old: int = days_old
        self.__status: str = status

    def age(self) -> None:
        """
        Increase the age of the plant by one day.
        """
        self.__days_old += 1

    def grow(self) -> None:
        """
        Increase the height of the plant by one centimeter.
        """
        self.__height += 1

    def set_height(self, height: int) -> None:
        """
        Update the plant height with validation.

        Rejects non-integer or negative values.
        """
        if type(height) is not int:
            print("""
Invalid operation attempted: height {height}cm [REJECTED]
Security: Non Interger height rejected
                  """)
        elif height < 0:
            print("""
Invalid operation attempted: height {height}cm [REJECTED]
Security: Negative height rejected
                  """)
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_status(self, status: str) -> None:
        """
        Update the plant status with validation.

        Accepted values: Plant, FloweringPlant, PrizeFlower.
        """
        if type(status) is not str:
            print("""
Invalid operation attempted: status -> {status} [REJECTED]
Security: Non String status rejected
                  """)
        elif status not in {"Plant", "FloweringPlant", "PrizeFlower"}:
            print("""
Invalid operation attempted: status -> {status} [REJECTED]
Security: Non valid status value rejected
                  """)
        else:
            self.__status = status
            print(f"Status updated: {self.__status} [OK]")

    def set_age(self, age: int) -> None:
        """
        Update the plant age with validation.
        """
        if type(age) is not int:
            print("""
Invalid operation attempted: age {age} days [REJECTED]
Security: Non Interger age rejected
                  """)
        elif age < 0:
            print("""
Invalid operation attempted: age {age}cm [REJECTED]
Security: Negative age rejected
                  """)
        else:
            self.__days_old = age
            print(f"Height updated: {self.__days_old} days [OK]")

    def get_status(self) -> str:
        """
        Return the plant status.
        """
        return self.__status

    def get_height(self) -> int:
        """
        Return the plant height.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Return the plant age.
        """
        return self.__days_old

    def get_info(self) -> None:
        """
        Print basic plant information.
        """
        print(f"{self.name} : {self.__height}cm, {self.__days_old} days old")


# ====================================================================


class Flower(Plant):
    """
    Represents a flowering plant with bloom behavior.
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
        """
        super().__init__(name, height, days_old, status)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        """
        Trigger blooming if the flower has not bloomed yet.
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
        print(f"{self.name} (Flower): {self.get_height()}cm, "
              f"{self.get_age()} days old, color : {self.color}")


class Tree(Plant):
    """
    Represents a tree capable of producing shade.
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
        """
        super().__init__(name, height, days_old, status)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and display the shade area produced by the tree.
        """
        shade_area: float = \
            self.get_height() // 2 * self.trunk_diameter * 7 / 10000
        print(f"{self.name} provides {round(shade_area, 2)} "
              f"square meters of shade")

    def get_info(self) -> None:
        """
        Print detailed information about the tree.
        """
        print(f"{self.name} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days old, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant with harvest information.
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
        """
        super().__init__(name, height, days_old, status)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        """
        Print detailed information about the vegetable.
        """
        print(f"{self.name} (Vegetable): {self.get_height()}cm, "
              f"{self.get_age()} days old, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


# ====================================================================


class Garden:
    """
    Represents a garden containing multiple plants.
    """

    def __init__(
            self,
            owner: str,
            name: str,
            plants: list[Plant | Flower | Tree | Vegetable] = []
            ):
        """
        Initialize a Garden instance.
        """
        self.owner = owner
        self.name = name
        self.__plants = plants
        self.__total_growth = 0

    def add_plant(self, plant: Plant | Flower | Tree | Vegetable) -> None:
        """
        Add a plant to the garden.
        """
        self.__plants = self.__plants + [plant]
        print(f"Added {plant.name} to {self.name}'s garden")

    def garden_growth(self) -> None:
        """
        Grow all plants in the garden by one unit.
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow()
            self.__total_growth += 1
            print(f"{plant.name} grew 1 cm")

    def height_validation(self) -> None:
        """
        Perform a height validation test on the garden.
        """
        total_height = 0
        for plant in self.__plants:
            if type(plant) is Tree:
                total_height += plant.get_height() // 5
            elif type(plant) is Vegetable:
                total_height += plant.get_height() * 2
            else:
                total_height += plant.get_height()

        print("Height validation test:",
              total_height / len(self.__plants) > 30)

    def garden_score(self) -> int:
        """
        Calculate and return the garden score.
        """
        score = 0
        for plant in self.__plants:
            score += plant.get_height() + plant.get_age() * 2
            if plant.get_status() == "PrizeFlower":
                score += 10
        return score

    def get_plants(self):
        """Return all plants in the garden."""
        return self.__plants

    def get_total_growth(self) -> int:
        """Return total growth accumulated."""
        return self.__total_growth


# ====================================================================


class GardenManager:
    """
    Manages multiple gardens and provides analytics.
    """

    def __init__(self, gardens: dict[str, Garden] = {}):
        """Initialize GardenManager."""
        self.__gardens = gardens

    class GardenStats:
        """
        Utility class for garden statistics.
        """

        @staticmethod
        def display_garden_stats(garden: Garden) -> None:
            """
            Display statistics for a given garden.
            """
            plants_status = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            plants = garden.get_plants()

            print(f"==== {garden.name} Report ====")
            for plant in plants:
                print(f"- {plant.name}: {plant.get_height()}cm", end="")
                if type(plant) is Flower:
                    print(f", {plant.color} flowers", end="")
                if plant.get_status() == "FloweringPlant":
                    print(" (blooming)", end="")
                if plant.get_status() == "PrizeFlower":
                    print(" (blooming), Prize points: 10", end="")
                plants_status[plant.get_status()] += 1
                print()

            print(f"\nPlants added: {len(plants)}, "
                  f"Total growth: {garden.get_total_growth()}cm")

            print(f"Plant Type: \
{plants_status['Plant']} Regular, \
{plants_status['FloweringPlant']} Flowering, \
{plants_status['PrizeFlower']} Prize flower")

    def add_garden(self, garden: Garden) -> None:
        """
        Add a garden to the manager.
        """
        if type(garden) is not Garden:
            print("Invalid garden type")
        elif garden.name in self.__gardens:
            print("Garden already exists")
        else:
            self.__gardens[garden.name] = garden

    @classmethod
    def create_garden_network(cls, manager: "GardenManager") -> None:
        """
        Generate and display network-wide garden analytics.
        """
        gardens = manager.get_gardens()

        total_plants = 0
        total_score = 0
        best_name = None
        best_score = 0

        print("===== Garden Network Analytics =====")

        for name, garden in gardens.items():
            score = garden.garden_score()
            count = len(garden.get_plants())
            total_plants += count
            total_score += score
            print(f"- {name}: {count} plants, score {score}")

            if score > best_score:
                best_score = score
                best_name = name

        print("\n===== Network Summary =====")
        print(f"Total gardens: {len(gardens)}")
        print(f"Total plants: {total_plants}")
        print(f"Total network score: {total_score}")
        print(f"Best garden: {best_name} ({best_score})")

    def compare_gardens_score(self) -> None:
        """
        Compare scores of all gardens.
        """
        print("Garden scores - " + ", ".join(
            f"{name}: {garden.garden_score()}"
            for name, garden in self.__gardens.items()
        ))

    def get_gardens(self):
        """Return managed gardens."""
        return self.__gardens


# ====================================================================


if __name__ == "__main__":
    print("=== Garden Management System Demo ===", end="\n\n")
    garden_manager: GardenManager = GardenManager(
            {"Alice's Garden": Garden("Alice's Garden", "Alice"),
             "Theo's Garden": Garden("Theo's Garden", "Theo", [
                 Flower("Rose", 21, 30, "Plant", "red")
                 ])})
    garden_manager.get_gardens()["Alice's Garden"].add_plant(
            Tree("Oak", 100, 150, "Plant", 20))
    garden_manager.get_gardens()["Alice's Garden"].add_plant(
            Flower("Rose", 21, 30, "FloweringPlant", "red"))
    garden_manager.get_gardens()["Alice's Garden"].add_plant(
            Flower("Sunflower", 50, 25, "PrizeFlower", "yellow"))
    print()
    garden_manager.get_gardens()["Alice's Garden"].garden_growth()

    print()
    garden_manager.GardenStats.display_garden_stats(
            garden_manager.get_gardens()["Alice's Garden"])

    print()
    garden_manager.get_gardens()["Alice's Garden"].height_validation()
    garden_manager.compare_gardens_score()
    print(f"Total Garden managed: {len(garden_manager.get_gardens())}")
