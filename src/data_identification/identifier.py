# src/data_identification/identifier.py
import numpy as np
from typing import Dict, Any, Union
from pathlib import Path

class SeismicDataIdentifier:
    """
    Handles identification and basic validation of seismic data files.
    """
    def __init__(self):
        self.supported_formats = {
            'segy': ['segy', 'sgy'],
            'segd': ['segd', 'sgd'],
            'su': ['su'],
            'rsf': ['rsf']
        }

    def identify_data_format(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Identify the format and basic characteristics of a seismic data file.

        Args:
            file_path (Union[str, Path]): Path to the seismic data file

        Returns:
            Dict[str, Any]: Dictionary containing format information and basic metadata
        """
        path = Path(file_path)
        extension = path.suffix.lower().lstrip('.')

        # Identify file format
        format_type = self._get_format_type(extension)

        # Basic file metadata
        metadata = {
            'format': format_type,
            'filename': path.name,
            'size': path.stat().st_size if path.exists() else None,
            'extension': extension
        }

        return metadata

    def _get_format_type(self, extension: str) -> str:
        """Determine the format type based on file extension."""
        for format_type, extensions in self.supported_formats.items():
            if extension in extensions:
                return format_type
        return 'unknown'

    def validate_format(self, file_path: Union[str, Path]) -> bool:
        """Check if the file format is supported."""
        path = Path(file_path)
        extension = path.suffix.lower().lstrip('.')
        return any(extension in exts for exts in self.supported_formats.values())