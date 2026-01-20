def garden_operations(error: int) -> None:
    """
    Perform an operation that intentionally raises different exceptions.

    The type of exception raised depends on the value of the `error` parameter.

    Args:
        error (int): Determines which error to trigger.
            0 -> ValueError
            1 -> ZeroDivisionError
            2 -> FileNotFoundError
            3 -> KeyError
    """
    if error == 0:
        print("Testing ValueError...")
        test: int = int("abc")
        print(test)
    elif error == 1:
        print("Testing ZeroDivisionError...")
        test1: float = 14 / 0
        print(test1)
    elif error == 2:
        print("Testing FileNotFoundError...")
        test2 = open("missing.txt")
        print(test2)
    elif error == 3:
        print("Testing KeyError...")
        test3: dict[str, int] = {"a": 0, "b": 0}
        print(test3["c"])


def test_error_types() -> None:
    """
    Demonstrate handling of multiple built-in Python exception types.

    This function intentionally triggers and catches several common errors:
    ValueError, ZeroDivisionError, FileNotFoundError, and KeyError,
    showing that the program can continue running after each error.
    """
    print("=== Garden Error Types Demo ===")

    print()
    for error in range(4):
        try:
            garden_operations(error)
        except (ValueError, FileNotFoundError, ZeroDivisionError, KeyError) \
                as err:
            print(f"{err.__class__.__name__} Error: {err}")
        print()

    print("Testing multiple errors together...")

    print()
    print("Caught an error, but program continues!")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
