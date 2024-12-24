import numpy as np
from pathlib import Path
from typing import Dict, Any, Union

class SeismicDataIdentifier:
    def __init__(self):
        self.supported_formats = {
            'segy': ['segy', 'sgy'],
            'segd': ['segd', 'sgd'],
            'su': ['su'],
            'rsf': ['rsf']
        }
    
    def identify_data_format(self, data_path: str) -> str:
        """
        Identify the format of the seismic data file.
        
        Args:
            data_path (str): Path to the seismic data file
            
        Returns:
            str: Identified format
        """
        path = Path(data_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {data_path}")
            
        extension = path.suffix.lower().lstrip('.')
        
        for format_name, extensions in self.supported_formats.items():
            if extension in extensions:
                return format_name
                
        return "unknown"
    
    def analyze_seismic_data(self, data_path: str) -> Dict[str, Any]:
        """
        Analyze seismic data file and extract metadata.
        
        Args:
            data_path (str): Path to seismic data file
            
        Returns:
            Dict[str, Any]: Analysis results including format and metadata
        """
        path = Path(data_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {data_path}")
            
        format_type = self.identify_data_format(data_path)
        
        return {
            'format': format_type,
            'file_size': path.stat().st_size,
            'last_modified': path.stat().st_mtime,
            'status': 'success'
        }
