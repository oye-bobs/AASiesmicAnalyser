import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, Optional, Union, List
import seaborn as sns

class AdvancedPlotter:
    def __init__(self):
        self.fig_size = (12, 8)
        self.dpi = 100
        plt.style.use('seaborn')
        
    def plot_spectrogram(self, data: np.ndarray, sample_rate: float,
                        save_path: Optional[str] = None):
        """Plot spectrogram."""
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        plt.specgram(data, Fs=1/sample_rate)
        plt.title("Spectrogram")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.colorbar(label="Amplitude")
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
        
    def plot_amplitude_spectrum(self, data: np.ndarray, sample_rate: float,
                              save_path: Optional[str] = None):
        """Plot amplitude spectrum."""
        freqs = np.fft.fftfreq(len(data), d=sample_rate)
        spectrum = np.abs(np.fft.fft(data))
        
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2])
        plt.title("Amplitude Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
        
    def plot_statistical_distribution(self, data: np.ndarray,
                                    save_path: Optional[str] = None):
        """Plot statistical distribution."""
        plt.figure(figsize=self.fig_size, dpi=self.dpi)
        sns.histplot(data, kde=True)
        plt.title("Amplitude Distribution")
        plt.xlabel("Amplitude")
        plt.ylabel("Count")
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
