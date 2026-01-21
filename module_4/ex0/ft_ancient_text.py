from typing import TextIO


def data_recovery(file_name: str) -> None:
    """
    Recover and display the contents of a storage file.

    This function attempts to open a file in read mode.
    If the file exists, its contents are printed.
    If the file does not exist or cannot be opened,
    an error message is displayed.

    Args:
        file_name (str): Name of the file to recover.

    Returns:
        None
    """
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file: TextIO = open(file_name, "r")
    except Exception:
        print("ERROR: Storage vault not found.")
    else:
        print("""Connection established...

RECOVERED DATA:""")
        print(file.read())
        file.close()

        print()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print()
    data_recovery("ancient_fragment.txt")
