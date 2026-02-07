#!/usr/bin/env python3

from typing import TextIO


def data_recovery(file_name: str) -> None:
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


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print()
    data_recovery("ancient_fragment.txt")


if __name__ == "__main__":
    main()
