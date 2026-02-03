import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    print()
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_air())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print()
    print("Testing direct module access:")
    print("alchemy.create_fire():", alchemy.create_fire())
    print("alchemy.create_water():", alchemy.create_water())
    try:
        print("alchemy.create_earth():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
