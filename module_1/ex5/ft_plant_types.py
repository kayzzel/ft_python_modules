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
        self.__height: int = height
        self.__days_old: int = days_old

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
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

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
            self.__days_old = age
            print(f"Height updated: {self.__days_old} days [OK]")

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            int: Height of the plant in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            int: Age of the plant in days.
        """
        return self.__days_old

    def get_info(self) -> None:
        """
        Print the plant's name, height, and age.
        """
        print(f"{self.name} : {self.__height}cm, {self.__days_old} days old")


class Flower(Plant):
    """
    Represents a flowering plant with a color and blooming behavior.
    """

    def __init__(
            self,
            name: str = "Iris",
            height: int = 10,
            days_old: int = 30,
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
        print(f"{self.name} (Flower): {self.get_height()}cm, "
              f"{self.get_age()} days old, color : {self.color}")


class Tree(Plant):
    """
    Represents a tree with a trunk diameter and shade-producing capability.
    """

    def __init__(
            self,
            name: str = "Oak",
            height: int = 500,
            days_old: int = 365,
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
        super().__init__(name, height, days_old)
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
    Represents a vegetable plant with harvest and nutritional information.
    """

    def __init__(
            self,
            name: str = "Tomato",
            height: int = 80,
            days_old: int = 90,
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
        super().__init__(name, height, days_old)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        """
        Print detailed information about the vegetable.
        """
        print(f"{self.name} (Vegetable): {self.get_height()}cm, "
              f"{self.get_age()} days old, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("==== Garden Plant Type ====")

    print()
    print("=== Flowers ===")
    flower: Flower = Flower()
    flower.get_info()
    flower.bloom()
    print()
    flower2: Flower = Flower("Lycoris radiata", 25, 30, "red")
    flower2.get_info()
    flower2.bloom()

    print()
    print("=== Trees ===")
    tree: Tree = Tree()
    tree.get_info()
    tree.produce_shade()
    print()
    tree2: Tree = Tree("Birch", 50, 60, 10)
    tree2.get_info()
    tree2.produce_shade()

    print()
    print("=== Vegetables ===")
    vegetable: Vegetable = Vegetable()
    vegetable.get_info()
    print()
    vegetable2: Vegetable = Vegetable("Carrot", 20, 60, "spring", "calcium")
    vegetable2.get_info()
