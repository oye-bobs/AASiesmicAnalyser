# tests/test_identifier.py
import pytest
from src.data_identification import SeismicDataIdentifier
from pathlib import Path

def test_identifier_initialization():
    identifier = SeismicDataIdentifier()
    assert isinstance(identifier.supported_formats, dict)
    assert 'segy' in identifier.supported_formats

def test_format_identification():
    identifier = SeismicDataIdentifier()
    test_file = Path("test_file.sgy")
    metadata = identifier.identify_data_format(test_file)
    assert metadata['format'] == 'segy'
    assert metadata['extension'] == 'sgy'

def test_unsupported_format():
    identifier = SeismicDataIdentifier()
    test_file = Path("test_file.xyz")
    metadata = identifier.identify_data_format(test_file)
    assert metadata['format'] == 'unknown'