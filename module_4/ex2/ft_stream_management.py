import sys


def stream_management() -> None:
    """
    Handle a three-channel communication stream using standard input,
    standard output, and standard error.

    The function prompts the user for an archivist ID and a status report.
    Messages are printed to different output streams to simulate a
    communication system diagnostic.

    Returns:
        None
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===", file=sys.stdout)

    print()
    id: str = input("Input Stream active. Enter archivist ID: ")
    if id is None or id == "":
        print("[ALERT] No Archivist Id Was Provided", file=sys.stderr)
        return
    report: str = input("Input Stream active. Enter status report: ")
    if report is None or id == "":
        print("[ALERT] No Report Was Provided", file=sys.stderr)
        return

    print()
    print(f"[STANDARD] Archive status from {id}: {report}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channel verified",
          file=sys.stderr)
    print("[STANDARD] Data transimtion complete", file=sys.stdout)

    print()
    print("Three-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    stream_management()
