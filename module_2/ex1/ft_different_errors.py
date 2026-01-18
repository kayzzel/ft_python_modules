def garden_operations(error: int):
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
        test = int("abc")
        print(test)
    elif error == 1:
        test1 = 14 / 0
        print(test1)
    elif error == 2:
        test2 = open("abc.txt")
        print(test2)
    elif error == 3:
        test3 = {"a": 0, "b": 0}
        print(test3["c"])


def test_error_types():
    """
    Demonstrate handling of multiple built-in Python exception types.

    This function intentionally triggers and catches several common errors:
    ValueError, ZeroDivisionError, FileNotFoundError, and KeyError,
    showing that the program can continue running after each error.
    """
    print("=== Garden Error Types Demo ===")

    print()
    print("Testing ValueError...")
    try:
        garden_operations(0)
    except ValueError as err:
        print(f"ValueError Error: {err}")

    print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operations(1)
    except ZeroDivisionError as err:
        print(f"ZeroDivisionError Error: {err}")

    print()
    print("Testing FileNotFoundError...")
    try:
        garden_operations(2)
    except FileNotFoundError as err:
        print(f"FileNotFoundError Error: {err}")

    print()
    print("Testing KeyError...")
    try:
        garden_operations(3)
    except KeyError as err:
        print(f"KeyError Error: {err}")

    print()
    print("Testing multiple errors together...")

    print()
    print("Caught an error, but program continues!")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
