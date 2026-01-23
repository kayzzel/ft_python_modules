def secure_extraction(file_name: str, content: str) -> None:
    """
    Open a file in append-plus mode to securely read its current contents
    and append new data without overwriting existing information.

    The function:
    - Opens the file using "a+" mode (read + append)
    - Reads and displays existing file content
    - Appends new content to the end of the file
    - Handles file-related errors gracefully

    Args:
        file_name (str): Name of the file acting as the secure vault.
        content (str): Text to append to the vault.
    """
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
