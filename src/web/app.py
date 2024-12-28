from flask import Flask, request, jsonify
from src.data_loading import SeismicDataLoader
from src.analysis.advanced_analysis import AdvancedAnalysis
from src.visualization.advanced_plotter import AdvancedPlotter

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)
    
    # Load data
    loader = SeismicDataLoader()
    data, headers = loader.load_file(file_path)
    
    # Perform analysis
    analyzer = AdvancedAnalysis()
    spectral_attrs = analyzer.compute_spectral_attributes(data[0], headers['sample_rate'])
    
    # Generate visualizations (you can extend this)
    plotter = AdvancedPlotter()
    plotter.plot_spectrogram(data[0], headers['sample_rate'], "output/spectrogram.png")
    
    return jsonify({"message": "Analysis complete", "spectrogram": "output/spectrogram.png"})

if __name__ == '__main__':
    app.run(debug=True)
