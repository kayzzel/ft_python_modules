import math


def get_distance(
    coord_1: tuple[int, int, int],
    coord_2: tuple[int, int, int]
) -> float:
    """
    Compute the Euclidean distance between two 3D coordinates.

    Args:
        coord_1 (tuple[int, int, int]): First coordinate (x, y, z).
        coord_2 (tuple[int, int, int]): Second coordinate (x, y, z).

    Returns:
        float: Distance between the two coordinates.
    """
    distance: float = (coord_2[0] - coord_1[0]) ** 2
    distance += (coord_2[1] - coord_1[1]) ** 2
    distance += (coord_2[2] - coord_1[2]) ** 2
    return math.sqrt(distance)


def parse_coords(coords: str) -> tuple[int, int, int]:
    """
    Parse a coordinate string into a 3D integer tuple.

    Args:
        coords (str): Coordinate string formatted as "x,y,z".

    Returns:
        tuple[int, int, int]: Parsed coordinates.

    Raises:
        ValueError: If conversion to integers fails.
        IndexError: If the coordinate format is invalid.
    """
    coords_str: list[str] = coords.split(",", 3)
    return int(coords_str[0]), int(coords_str[1]), int(coords_str[2])


def tuple_unpacking(coords: tuple[int, int, int]) -> None:
    """
    Demonstrate tuple unpacking using a 3D coordinate.

    Args:
        coords (tuple[int, int, int]): Coordinate to unpack.

    Returns:
        None
    """
    x: int
    y: int
    z: int
    x, y, z = coords

    print("Unpacking demonstration:")
    print(f"player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def is_coord_tuple_valid(coords: object) -> bool:
    """
    Validate whether an object is a valid 3D integer coordinate tuple.

    Args:
        coords (object): Object to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if type(coords) is not tuple:
        print("Error: coords type is not a tuple")
        return False

    if len(coords) != 3:
        print(f"Error: coord has the wrong number of elements ({len(coords)})")
        return False

    if (
        type(coords[0]) is not int
        or type(coords[1]) is not int
        or type(coords[2]) is not int
    ):
        print("Error: all coords elements are not integers")
        return False

    return True


def coords_comp(coords: str | tuple[int, int, int]) -> None:
    """
    Compare coordinates by parsing or validating them and
    computing the distance from the origin (0, 0, 0).

    Args:
        coords (str | tuple[int, int, int]):
            Coordinates as a string ("x,y,z") or a tuple.

    Returns:
        None
    """
    coords_tuple: tuple[int, int, int] = (0, 0, 0)

    if type(coords) is str:
        try:
            coords_tuple = parse_coords(coords)
        except Exception as err:
            print(f"Parsing Invalid Coords: \"{coords}\"")
            print("Error:", err)
            print(
                f"Error detail - Type {err.__class__.__name__}, "
                f"Args: (\"{err}\")"
            )
            return
        else:
            print(f"Parsing Coords: \"{coords}\"")
            print(f"Parsed Position: {coords_tuple}")

    elif is_coord_tuple_valid(coords):
        coords_tuple = coords
        print(f"Position created: {coords}")

    else:
        return

    distance: float = get_distance((0, 0, 0), coords_tuple)
    print(f"distance between (0, 0, 0) and {coords_tuple} is {distance}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print()
    coords_comp((10, 20, 5))

    print()
    coords_comp("3,4,0")

    print()
    coords_comp("abc,def,ghi")

    print()
    tuple_unpacking((3, 4, 0))
