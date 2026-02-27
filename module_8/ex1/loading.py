#!/usr/bin/env python3

import sys
from importlib import import_module
from importlib.metadata import version, PackageNotFoundError

REQUIRED_PACKAGES: list[str] = ["pandas", "numpy", "matplotlib"]


def detect_environment() -> str:
    if hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix:
        return "Virtualenv"
    return "System Python"


def check_dependencies() -> list[str]:
    """Check if required packages are installed and print versions"""

    print("Checking dependencies:")
    missing: list[str] = []

    # Trying for each module to import it with import_module
    # if there is an error print the appropriate message
    for package in REQUIRED_PACKAGES:
        try:
            import_module(package)
            pkg_version: str = version(package)
            print(f"[OK] {package} ({pkg_version}) - Ready")

        except ModuleNotFoundError:
            print(f"[MISSING] {package} - Not installed")
            missing.append(package)

        except PackageNotFoundError:
            print(f"[WARNING] {package} - Version info not found")

    return missing


def print_install_instructions(missing: list[str]) -> None:
    """Show pip vs Poetry installation instructions"""

    print("\nMissing dependencies detected.\n")

    print("Install with pip:")
    print("  pip install -r requirements.txt")

    print("\nInstall with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")

    print("\nMissing packages:", ", ".join(missing))


def analyze_matrix_data() -> None:
    """Simulate matrix data and perform analysis"""

    print("\nAnalyzing Matrix data...")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")

    # Simulated matrix (100x10)
    matrix: np.ndarray[tuple[int, int], np.dtype[np.float64]] = (
        np.random.randn(1000).reshape(100, 10)
            )
    # Creating the dataframe
    df: pd.DataFrame = pd.DataFrame(matrix)

    # Puting in the mean part the result of the "mean" of each row
    df["mean"] = df.mean(axis=1)

    print("Generating visualization...")

    # Creationg the graph, puting the value in and saving it
    plt.figure()
    plt.plot(df["mean"])
    plt.title("Matrix Mean Values")
    plt.xlabel("Row Index")
    plt.ylabel("Mean Value")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def compare_management() -> None:
    """Explain pip vs Poetry differences"""
    print("\nDependency Management Comparison:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml with locked dependencies")
    print("- Poetry creates isolated virtual environments automatically")
    print("- pip requires manual virtualenv management")


def main():
    print("LOADING STATUS: Loading programs...")
    print(f"Environment detected: {detect_environment()}")

    missing: list[str] = check_dependencies()

    if missing:
        print_install_instructions(missing)
        sys.exit(1)

    analyze_matrix_data()
    compare_management()


if __name__ == "__main__":
    main()
