import click
import numpy as np
from pathlib import Path
from .data_loading import SeismicDataLoader
from .analysis.advanced_analysis import AdvancedAnalysis
from .visualization.advanced_plotter import AdvancedPlotter

@click.group()
def cli():
    """Seismic data analysis tool."""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output-dir', '-o', default='output', 
              help='Output directory for plots and results')
@click.option('--plot-type', '-p', multiple=True,
              type=click.Choice(['trace', 'spectrum', 'spectrogram', 'stats']),
              default=['trace'],
              help='Types of plots to generate')
def analyze(input_file, output_dir, plot_type):
    """Analyze seismic data file."""
    # Create output directory
    out_path = Path(output_dir)
    out_path.mkdir(exist_ok=True)
    
    # Load data
    loader = SeismicDataLoader()
    data, headers = loader.load_file(input_file)
    
    # Perform analysis
    analyzer = AdvancedAnalysis()
    plotter = AdvancedPlotter()
    
    click.echo("Analyzing data...")
    
    # Generate plots
    for plot in plot_type:
        if plot == 'trace':
            plotter.plot_seismic_trace(
                data[0], headers['sample_rate'],
                save_path=out_path / 'trace.png'
            )
        elif plot == 'spectrum':
            plotter.plot_amplitude_spectrum(
                data[0], headers['sample_rate'],
                save_path=out_path / 'spectrum.png'
            )
        elif plot == 'spectrogram':
            plotter.plot_spectrogram(
                data[0], headers['sample_rate'],
                save_path=out_path / 'spectrogram.png'
            )
        elif plot == 'stats':
            plotter.plot_statistical_distribution(
                data[0], save_path=out_path / 'distribution.png'
            )
    
    click.echo(f"Results saved to {output_dir}")

if __name__ == '__main__':
    cli()
