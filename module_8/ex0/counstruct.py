from sys import prefix, base_prefix, executable, path
from os.path import basename


def main() -> None:
    if prefix == base_prefix:
        print("MATRIX STATUS: Your're still plugged in")

        print()
        print("Current Python:", executable)
        print("Virtual Environment: None detected")

        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate     # On Unix")

        print("matrix_env")
        print("Scripts")
        print("activate    # On Windows")

        print()
        print("Then run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct")

        print()
        print("Current Python:", executable)
        print("Virtual Environment:", basename(prefix))
        print("Environment Path:", prefix)

        print("""
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
""")

        print("Package installation path:")
        print(path[-1])


if __name__ == "__main__":
    main()
