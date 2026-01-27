#!/usr/bin/env python3

from typing import Generator
from time import perf_counter
from random import randint


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generate the first `n` Fibonacci numbers.

    Args:
        n (int): Number of Fibonacci values to generate.

    Yields:
        int: Next Fibonacci number.
    """
    a: int = 0
    b: int = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int) -> Generator[int, None, None]:
    """
    Generate the first `n` prime numbers.

    Args:
        n (int): Number of prime numbers to generate.

    Yields:
        int: Next prime number.
    """
    nbr: int = 2

    while n > 0:
        divider: int = 2
        limit: int = nbr // 2 + 1
        is_prime: bool = True

        while divider < limit:
            if nbr % divider == 0:
                is_prime = False
                break
            divider += 1

        if is_prime:
            yield nbr
            n -= 1

        nbr += 1


def event_generator(n: int) -> Generator[str, None, None]:
    """
    Generate a stream of random game events.

    Args:
        n (int): Number of events to generate.

    Yields:
        str: Formatted game event string.
    """
    event_list: list[str] = [
        "kill by Frank",
        "quest_complete by Grace",
        "level_up by Jack",
        "level_up by Frank",
        "level_up by Olivia",
        "kill by Noah",
        "quest_complete by Alice",
        "level_up by Noah",
        "item_found by Diana",
        "level_up by Bob"
    ]

    for index in range(n):
        event: str = event_list[randint(0, 9)]
        yield f"Event {index}: {event}"


def fibonacci_print(n: int) -> None:
    """
    Print the first `n` Fibonacci numbers.

    Args:
        n (int): Number of Fibonacci values to print.

    Returns:
        None
    """
    print(f"Fibonacci sequence (first {n}) ", end="")

    first: bool = True
    for nbr in fibonacci_generator(n):
        if not first:
            print(", ", end="")
        print(nbr, end="")
        first = False

    print()


def prime_print(n: int) -> None:
    """
    Print the first `n` prime numbers.

    Args:
        n (int): Number of prime numbers to print.

    Returns:
        None
    """
    print(f"Prime Numbers (first {n}) ", end="")

    first: bool = True
    for nbr in prime_generator(n):
        if not first:
            print(", ", end="")
        print(nbr, end="")
        first = False

    print()


def print_game_event(n: int) -> None:
    """
    Print a stream of game events and analyze the event data.

    Displays:
      - First 3 events
      - Event summary statistics

    Args:
        n (int): Number of events to process.

    Returns:
        None
    """
    event_count: int = 0
    treasure: int = 0
    level_up: int = 0

    for event in event_generator(n):
        if event_count < 3:
            print(event)
        elif event_count == 3:
            print("...")

        event_count += 1

        if "item_found" in event:
            treasure += 1
        if "level_up" in event:
            level_up += 1

    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", event_count)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    print()
    start: float = perf_counter()
    print_game_event(1000)
    end: float = perf_counter()

    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f}")

    print()
    print("=== Generator Demonstration ===")
    fibonacci_print(10)
    prime_print(5)
