#!/usr/bin/env python3

from typing import TextIO


def data_storage(file_name: str, to_write: str) -> None:
    print(f"Initializing new storage unit: {file_name}")
    try:
        file: TextIO = open(file_name, "w")
        print("""Storage unit created successfully...

Inscribing preservation data...""")
        file.write(to_write)
    except Exception as err:
        print(f"{err.__class__.__name__} Error: {err}")
    else:
        print(to_write)

        print()
        print(f"Data inscription complete. Storage unit sealed.\n\
Archive {file_name} ready for long-term preservation.")
        file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print()
    data_storage(
            "new_discovery.txt",
            """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee""")


if __name__ == "__main__":
    main()
