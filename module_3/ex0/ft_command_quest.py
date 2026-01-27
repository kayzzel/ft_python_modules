#!/usr/bin/env python3

import sys


def display_args() -> None:
    """
    Display command-line arguments passed to the program.

    The function reads `sys.argv` and prints:
      - The program name
      - The number of arguments (excluding the program name)
      - Each argument with its index
      - Total number of arguments including program name

    Returns:
        None
    """
    print("=== Command Quest ===")
    args: list[str] = sys.argv

    if len(args) <= 1:
        print("No arguments provided!")

    print(f"Program name: {args[0]}")

    if len(args) > 1:
        print(f"Arguments received: {len(args) - 1}")

    for index in range(1, len(args)):
        print(f"Arguments {index}: {args[index]}")

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    display_args()
