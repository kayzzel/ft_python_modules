#!/usr/bin/env python3

import sys


def pars_inventory() -> dict[str, int]:
    """
    Parse inventory items from command-line arguments.

    Expected argument format:
        item:quantity

    Returns:
        dict[str, int]: Dictionary mapping item names to quantities.
        Returns an empty dictionary if parsing fails or no items are provided.
    """
    args: list[str] = sys.argv
    inventory: dict[str, int] = {}

    if len(args) <= 1:
        print("No Items given for invertory management!!!")
        return {}

    try:
        for arg in args[1:]:
            item, quantity = arg.split(":", 1)
            inventory[item] = int(quantity)
    except Exception as err:
        print("Wrong item format")
        print(f"{err.__class__.__name__} Error: {err}")
        return {}
    else:
        return inventory


def total_item_inventory(inventory: dict[str, int]) -> None:
    """
    Display total and unique item counts in the inventory.

    Args:
        inventory (dict[str, int]): Inventory dictionary.

    Returns:
        None
    """
    total_item: int = 0
    unique_item: int = 0

    print("=== Inventory System Analysis ===")

    for quantity in inventory.values():
        unique_item += 1
        total_item += quantity

    print(f"Total items in inventory: {total_item}")
    print(f"Unique item type: {unique_item}")


def print_inventory(inventory: dict[str, int]) -> None:
    """
    Print inventory contents with percentage distribution.

    Args:
        inventory (dict[str, int]): Inventory dictionary.

    Returns:
        None
    """
    total_item: int = 0

    print("=== Current Inventory ===")

    for quantity in inventory.values():
        total_item += quantity

    for item, quantity in inventory.items():
        percentage: float = quantity / total_item * 100
        print(f"{item}: {quantity} units ({percentage:.2f}%)")


def inventory_stat(inventory: dict[str, int]) -> None:
    """
    Display inventory statistics including most and least abundant items.

    Args:
        inventory (dict[str, int]): Inventory dictionary.

    Returns:
        None
    """
    first: bool = True
    abundance: dict[str, dict[str, int | str]] = {}

    print("=== Inventory Statistics ===")

    for item, quantity in inventory.items():
        if first:
            abundance["most"] = dict(name=item, quantity=quantity)
            abundance["least"] = dict(name=item, quantity=quantity)
            first = False
        else:
            if quantity > int(abundance["most"]["quantity"]):
                abundance["most"] = dict(name=item, quantity=quantity)
            if quantity < int(abundance["least"]["quantity"]):
                abundance["least"] = dict(name=item, quantity=quantity)

    print(f"Most abundant: {abundance['most']['name']} \
({abundance['most']['quantity']} units)")
    print(f"Least abundant: {abundance['least']['name']} \
({abundance['least']['quantity']} units)")


def item_categories(inventory: dict[str, int]) -> None:
    """
    Categorize inventory items into moderate and scarce groups.

    Moderate items have more than 4 units.
    Scarce items have 4 or fewer units.

    Args:
        inventory (dict[str, int]): Inventory dictionary.

    Returns:
        None
    """
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}

    print("=== Item Categories ===")

    for item, quantity in inventory.items():
        if quantity > 4:
            moderate[item] = quantity
        else:
            scarce[item] = quantity

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_suggestions(inventory: dict[str, int]) -> None:
    """
    Display restocking suggestions based on inventory levels.

    Items with fewer than 2 units are marked for restocking.

    Args:
        inventory (dict[str, int]): Inventory dictionary.

    Returns:
        None
    """
    to_restock: list[str] = []

    print("=== Management Suggestions ===")

    for item, quantity in inventory.items():
        if quantity < 2:
            to_restock += [item]

    print(f"Restock needed: {to_restock}")


def dict_propriety(dictionary: dict[str, int], search: str) -> None:
    """
    Display dictionary properties and test key existence.

    Prints:
      - list of keys
      - list of values
      - whether a given key exists

    Args:
        dictionary (dict[str, int]): Dictionary to analyze.
        search (str): Key to search for.

    Returns:
        None
    """
    keys: list[str] = []
    values: list[int] = []
    search_in_dict: bool = True

    for key, value in dictionary.items():
        keys += [key]
        values += [value]

    try:
        dictionary[search]
    except Exception:
        search_in_dict = False
    else:
        search_in_dict = True

    print(f"Dictionary Keys: {keys}")
    print(f"Dictionary Values: {values}")
    print(f"Sample lookup - '{search}' in inventory: {search_in_dict}")


if __name__ == "__main__":

    inventory: dict[str, int] = pars_inventory()
    if (len(inventory) > 0):
        total_item_inventory(inventory)

        print()
        print_inventory(inventory)

        print()
        inventory_stat(inventory)

        print()
        item_categories(inventory)

        print()
        management_suggestions(inventory)

        print()
        dict_propriety(inventory, "sword")
