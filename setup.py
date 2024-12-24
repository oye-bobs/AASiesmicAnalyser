# main.py
from src.data_identification import SeismicDataIdentifier
from pathlib import Path
import sys

def main():
    print("Seismic Data Cleaning AI")
    print("------------------------")

    # Initialize the identifier
    identifier = SeismicDataIdentifier()

    # Print supported formats
    print("\nSupported formats:")
    for format_type, extensions in identifier.supported_formats.items():
        print(f"- {format_type}: {', '.join(extensions)}")

    # You can add more functionality here as we develop the project

if __name__ == "__main__":
    main()