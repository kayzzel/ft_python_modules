#!/usr/bin/env python3

def secure_extraction(file_name: str, content: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print()
    print("Initiating secure vault access...")
    try:
        with open(file_name, "r") as file:
            print("Vault connection established with failsafe protocols")

            print()
            print("SECURE EXTRACTION:")
            print(file.read())
        with open(file_name, "a") as file:
            print()
            print("SECURE PRESERVATION:")
            file.write(content)
            print(content)
            print("Vault automatically sealed upon completion")
    except Exception as err:
        print(f"{err.__class__.__name__} Error: {err}")
    else:
        print()
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    secure_extraction("classified_data.txt",
                      "[CLASSIFIED] New security protocols archived")
