#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """
    Validate a temperature value given as a string.

    The function checks:
    - whether the input is a string
    - whether it can be converted to an integer
    - whether the integer falls within the safe plant range (0–40°C)

    Args:
        temp_str (str): Temperature value provided as a string.

    Returns:
        int: The validated temperature if valid.
        -1: If the input is invalid or out of range.
    """
    if type(temp_str) is not str:
        print("Error: data entered is not a string!")
        return (-1)

    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
    except (ValueError, TypeError):
        print(f"Error: {temp_str} is not a valid number")
        return (-1)
    else:
        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return (temp_int)
        return (-1)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")

    print()
    check_temperature("25")

    print()
    check_temperature("abc")

    print()
    check_temperature("100")

    print()
    check_temperature("-50")

    print()
    print("All error types tested successfully!")
