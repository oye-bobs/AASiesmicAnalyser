import pytest
import numpy as np
from src.quality_control.controller import QualityController

def test_quality_controller_init():
    controller = QualityController()
    assert hasattr(controller, "qc_results")
    
def test_quality_check():
    controller = QualityController()
    test_data = np.random.randn(1000)
    results = controller.quality_check(test_data)
    
    assert "completeness" in results
    assert "noise_assessment" in results
    assert "trace_continuity" in results
