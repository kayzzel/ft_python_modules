#!/usr/bin/env python3

import sys
import os
from importlib import import_module
from importlib.metadata import version, PackageNotFoundError

REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def detect_environment():
    if "POETRY_ACTIVE" in os.environ:
        return "Poetry"
    if hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix:
        return "Virtualenv (pip)"
    return "System Python (pip)"


def check_dependencies():
    print("Checking dependencies:")
    missing = []

    for package in REQUIRED_PACKAGES:
        try:
            import_module(package)
            pkg_version = version(package)
            print(f"[OK] {package} ({pkg_version}) - Ready")
        except ModuleNotFoundError:
            print(f"[MISSING] {package} - Not installed")
            missing.append(package)
        except PackageNotFoundError:
            print(f"[WARNING] {package} - Version info not found")

    return missing


def print_install_instructions(missing):
    print("\nMissing dependencies detected.\n")

    print("Install with pip:")
    print("  pip install -r requirements.txt")

    print("\nInstall with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")

    print("\nMissing packages:", ", ".join(missing))


def analyze_matrix_data():
    print("\nAnalyzing Matrix data...")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Processing 1000 data points...")

    # Simulated matrix (100x10)
    matrix = np.random.randn(1000).reshape(100, 10)

    df = pd.DataFrame(matrix)
    df["mean"] = df.mean(axis=1)

    print("Generating visualization...")

    plt.figure()
    plt.plot(df["mean"])
    plt.title("Matrix Mean Values")
    plt.xlabel("Row Index")
    plt.ylabel("Mean Value")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")
    print(f"Environment detected: {detect_environment()}")

    missing = check_dependencies()

    if missing:
        print_install_instructions(missing)
        sys.exit(1)

    analyze_matrix_data()


if __name__ == "__main__":
    main()
