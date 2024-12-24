import pytest
import numpy as np
from src.feature_extraction.extractor import FeatureExtractor

def test_feature_extractor_init():
    extractor = FeatureExtractor()
    assert hasattr(extractor, "features")
    
def test_feature_extraction():
    extractor = FeatureExtractor()
    test_data = np.random.randn(1000)
    features = extractor.extract_features(test_data)
    
    assert "amplitude_stats" in features
    assert "frequency_content" in features
    assert "snr" in features
