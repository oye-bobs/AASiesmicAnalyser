# examples/basic_usage.py
from src.data_identification import SeismicDataIdentifier
from pathlib import Path

def main():
    # Initialize the identifier
    identifier = SeismicDataIdentifier()

    # Example file path (you'll need to update this with a real file)
    file_path = Path("path/to/your/seismic_file.sgy")

    # Identify the file format
    try:
        metadata = identifier.identify_data_format(file_path)
        print("File Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()