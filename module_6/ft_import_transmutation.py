import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_air
from alchemy.potions import strenght_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===")

    print()
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print()
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print()
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print()
    print("Method 4 - Multiple import:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_air(): {create_air()}")
    print(f"strenght_potion(): {strenght_potion()}")

    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
