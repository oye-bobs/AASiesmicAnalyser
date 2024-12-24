import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, Optional, Union, List

class SeismicPlotter:
    def __init__(self):
        self.fig_size = (12, 8)
        self.dpi = 100
        
    def plot_seismic_trace(self, data: np.ndarray, sample_rate: float = 0.002,
                          title: str = "Seismic Trace", save_path: Optional[str] = None):
        """Plot a single seismic trace."""
        time = np.arange(len(data)) * sample_rate
        
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        plt.plot(time, data)
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
        
    def plot_frequency_spectrum(self, data: np.ndarray, sample_rate: float = 0.002,
                              save_path: Optional[str] = None):
        """Plot frequency spectrum of seismic data."""
        freqs, psd = np.fft.fftfreq(len(data), d=sample_rate), np.abs(np.fft.fft(data))
        
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        plt.plot(freqs[:len(freqs)//2], psd[:len(psd)//2])
        plt.title("Frequency Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
        
    def plot_qc_results(self, qc_results: Dict[str, Dict[str, Union[float, int]]], 
                       save_path: Optional[str] = None):
        """Plot quality control results."""
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        
        # Extract metrics ensuring they're numeric
        metrics = []
        labels = []
        
        if 'completeness' in qc_results:
            metrics.append(float(qc_results['completeness']['completeness_ratio']))
            labels.append('Completeness')
            
        if 'noise_assessment' in qc_results:
            # Convert noise to quality (1 - normalized_noise)
            noise = float(qc_results['noise_assessment']['background_noise'])
            max_noise = 1.0  # Assuming normalized noise
            metrics.append(1 - min(noise/max_noise, 1.0))
            labels.append('Signal Quality')
            
        if 'trace_continuity' in qc_results:
            metrics.append(float(qc_results['trace_continuity']['continuity_score']))
            labels.append('Continuity')
        
        if metrics and labels:
            plt.bar(labels, metrics)
            plt.title("Quality Control Metrics")
            plt.ylabel("Score")
            plt.ylim(0, 1)
            
            if save_path:
                plt.savefig(save_path)
        plt.close()
