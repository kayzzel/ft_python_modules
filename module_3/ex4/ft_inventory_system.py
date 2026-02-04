#!/usr/bin/env python3

import sys


def pars_inventory() -> dict[str, int]:
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
    total_item: int = 0
    unique_item: int = 0

    print("=== Inventory System Analysis ===")

    for quantity in inventory.values():
        unique_item += 1
        total_item += quantity

    print(f"Total items in inventory: {total_item}")
    print(f"Unique item type: {unique_item}")


def print_inventory(inventory: dict[str, int]) -> None:
    total_item: int = 0

    print("=== Current Inventory ===")

    for quantity in inventory.values():
        total_item += quantity

    for item, quantity in inventory.items():
        percentage: float = quantity / total_item * 100
        print(f"{item}: {quantity} units ({percentage:.2f}%)")


def inventory_stat(inventory: dict[str, int]) -> None:
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
    catergories: dict[str, dict[str, int]] = {"moderate": {}, "scarce": {}}

    print("=== Item Categories ===")

    for item, quantity in inventory.items():
        if quantity > 4:
            catergories["moderate"][item] = quantity
        else:
            catergories["scarce"][item] = quantity

    print(f"Moderate: {catergories['moderate']}")
    print(f"Scarce: {catergories['scarce']}")


def management_suggestions(inventory: dict[str, int]) -> None:
    to_restock: list[str] = []

    print("=== Management Suggestions ===")

    for item, quantity in inventory.items():
        if quantity < 2:
            to_restock += [item]

    print(f"Restock needed: {to_restock}")


def dict_propriety(dictionary: dict[str, int], search: str) -> None:
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


def main() -> None:
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


if __name__ == "__main__":
    main()
