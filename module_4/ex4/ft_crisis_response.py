#!/usr/bin/env python3

def crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print()
    try:
        with open("lost_archive.txt", "r"):
            pass
    except FileNotFoundError:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        print("""RESPONSE: Archive not found in storage matrix
STATUS: Crisis handled, system stable""")

    print()
    try:
        with open("classified_vault.txt", "w") as file:
            file.write("test")
    except PermissionError:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        print("""RESPONSE: Security protocols deny access
STATUS: Crisis handled, security maintained""")

    print()
    try:
        print("ROUTINE ACCES: Attempting access to \
'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            pass
    except Exception as err:
        print(f"{err.__class__.__name__} Error: {err}")
    else:
        print(f"SUCCESS: Archive recovered -'{file.read()}'")
        print("STATUS: Normal operations resumed")

    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
