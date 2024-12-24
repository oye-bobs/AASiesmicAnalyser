import numpy as np
from typing import Dict, Any, List

class QualityController:
    def __init__(self):
        self.qc_results = {}
        
    def quality_check(self, data: np.ndarray) -> Dict[str, Any]:
        """
        Perform quality control checks on seismic data.
        
        Args:
            data (np.ndarray): Seismic data to check
            
        Returns:
            Dict[str, Any]: Quality control results
        """
        results = {
            'completeness': self._check_completeness(data),
            'noise_assessment': self._assess_noise(data),
            'trace_continuity': self._check_continuity(data)
        }
        
        self.qc_results = results
        return results
        
    def _check_completeness(self, data: np.ndarray) -> Dict[str, Any]:
        """Check data completeness."""
        return {
            'missing_values': int(np.sum(np.isnan(data))),
            'zero_values': int(np.sum(data == 0)),
            'completeness_ratio': float(1 - np.sum(np.isnan(data)) / data.size)
        }
        
    def _assess_noise(self, data: np.ndarray) -> Dict[str, float]:
        """Assess noise levels."""
        return {
            'background_noise': float(np.std(data)),
            'peak_to_noise': float(np.ptp(data) / np.std(data))
        }
        
    def _check_continuity(self, data: np.ndarray) -> Dict[str, Any]:
        """Check trace continuity."""
        diff = np.diff(data, axis=0)
        return {
            'max_gap': float(np.max(np.abs(diff))),
            'mean_gap': float(np.mean(np.abs(diff))),
            'continuity_score': float(1 - np.sum(np.abs(diff) > np.std(diff) * 3) / len(diff))
        }
