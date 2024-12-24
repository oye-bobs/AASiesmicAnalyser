# Usage Examples

## Command Line Interface

Analyze a SEG-Y file:
```bash
siesmic analyze data/example.sgy --plot-type trace spectrum spectrogram
[200~Generate statistical plots:

siesmic analyze data/example.sgy --plot-type stats
~
from src.data_loading import SeismicDataLoader
from src.analysis.advanced_analysis import AdvancedAnalysis
from src.visualization.advanced_plotter import AdvancedPlotter

# Load data
loader = SeismicDataLoader()
data, headers = loader.load_file("data/example.sgy")

# Perform advanced analysis
analyzer = AdvancedAnalysis()
spectral_attrs = analyzer.compute_spectral_attributes(data[0], headers['sample_rate'])
statistics = analyzer.compute_statistics(data[0])
events = analyzer.detect_events(data[0])

# Create visualizations
plotter = AdvancedPlotter()
plotter.plot_spectrogram(data[0], headers['sample_rate'], "spectrogram.png")
plotter.plot_amplitude_spectrum(data[0], headers['sample_rate'], "spectrum.png")
plotter.plot_statistical_distribution(data[0], "distribution.png")
mkdir -p notebooks
cat > notebooks/analysis_example.ipynb << 'EOF'
{
"cells": [
{
"cell_type": "markdown",
"metadata": {},
"source": [
"# Seismic Data Analysis Example"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": [
"import numpy as np\n",
"from src.data_loading import SeismicDataLoader\n",
"from src.analysis.advanced_analysis import AdvancedAnalysis\n",
"from src.visualization.advanced_plotter import AdvancedPlotter"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Generate Sample Data"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": [
"# Generate synthetic data\n",
"sample_rate = 0.002\n",
"time = np.arange(0, 1, sample_rate)\n",
"frequency = 25\n",
"data = np.sin(2 * np.pi * frequency * time) + 0.1 * np.random.randn(len(time))"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Perform Analysis"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": [
"analyzer = AdvancedAnalysis()\n",
"spectral_attrs = analyzer.compute_spectral_attributes(data, sample_rate)\n",
"statistics = analyzer.compute_statistics(data)\n",
"events = analyzer.detect_events(data)\n",
"\n",
"print("Statistics:")\n",
"for key, value in statistics.items():\n",
" print(f"{key}: {value}")"
]
},
{
"cell_type": "markdown",
"metadata": {},
"source": [
"## Create Visualizations"
]
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": [
"plotter = AdvancedPlotter()\n",
"plotter.plot_spectrogram(data, sample_rate)\n",
"plotter.plot_amplitude_spectrum(data, sample_rate)\n",
"plotter.plot_statistical_distribution(data)"
]
}
],
"metadata": {
"kernelspec": {
"display_name": "Python 3",
"language": "python",
"name": "python3"
}
},
"nbformat": 4,
"nbformat_minor": 4
}
