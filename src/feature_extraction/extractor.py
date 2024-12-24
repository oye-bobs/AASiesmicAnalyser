import numpy as np
from scipy import signal
from typing import Dict, Any, List

class FeatureExtractor:
    def __init__(self):
        self.features = {}
        
    def extract_features(self, trace_data: np.ndarray) -> Dict[str, Any]:
        """
        Extract features from seismic trace data.
        
        Args:
            trace_data (np.ndarray): Seismic trace data
            
        Returns:
            Dict[str, Any]: Extracted features
        """
        features = {
            'amplitude_stats': self._compute_amplitude_stats(trace_data),
            'frequency_content': self._analyze_frequency(trace_data),
            'snr': self._calculate_snr(trace_data)
        }
        
        self.features = features
        return features
        
    def _compute_amplitude_stats(self, data: np.ndarray) -> Dict[str, float]:
        """Calculate amplitude statistics."""
        return {
            'mean': float(np.mean(data)),
            'std': float(np.std(data)),
            'max': float(np.max(data)),
            'min': float(np.min(data))
        }
        
    def _analyze_frequency(self, data: np.ndarray) -> Dict[str, Any]:
        """Analyze frequency content."""
        freqs, psd = signal.welch(data)
        return {
            'dominant_freq': float(freqs[np.argmax(psd)]),
            'freq_range': [float(freqs.min()), float(freqs.max())],
            'mean_psd': float(np.mean(psd))
        }
        
    def _calculate_snr(self, data: np.ndarray) -> float:
        """Calculate signal-to-noise ratio."""
        noise = data - signal.medfilt(data, kernel_size=5)
        signal_power = np.mean(data ** 2)
        noise_power = np.mean(noise ** 2)
        return float(10 * np.log10(signal_power / noise_power))
