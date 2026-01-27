#!/usr/bin/env python3

class SecurePlant:
    """
    Represents a plant with a name, height, and age in days. """

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
            print(f"""
Invalid operation attempted: height {height}cm [REJECTED]
Security: Non Interger height rejected
                  """)
        elif (height < 0):
            print(f"""
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
            print(f"""
Invalid operation attempted: age {age} days [REJECTED]
Security: Non Interger age rejected
                  """)
        elif (age < 0):
            print(f"""
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


if __name__ == "__main__":
    print("==== Garden Security System ====")
    plant: SecurePlant = SecurePlant()
    print("Secure Plant created : Iris")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.get_info()
