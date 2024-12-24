import pytest
import numpy as np
from src.data_identification.identifier import SeismicDataIdentifier

def test_seismic_identifier_init():
    identifier = SeismicDataIdentifier()
    assert isinstance(identifier.supported_formats, dict)
    assert 'segy' in identifier.supported_formats
    
def test_file_not_found():
    identifier = SeismicDataIdentifier()
    with pytest.raises(FileNotFoundError):
        identifier.analyze_seismic_data("nonexistent_file.sgy")

def test_identify_data_format():
    identifier = SeismicDataIdentifier()
    # Test with nonexistent file
    with pytest.raises(FileNotFoundError):
        identifier.identify_data_format("nonexistent_file.sgy")
