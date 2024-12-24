import numpy as np
import sys
import os

def main():
    try:
        from src.data_identification import SeismicDataIdentifier
        from src.feature_extraction import FeatureExtractor
        from src.quality_control import QualityController
        from src.visualization import SeismicPlotter
    except ImportError as e:
        print(f"Error importing required modules: {e}")
        print("Make sure all required modules are installed and in the correct location.")
        sys.exit(1)

    try:
        # Generate sample data
        print("Generating sample seismic data...")
        sample_rate = 0.002  # 2ms
        time = np.arange(0, 1, sample_rate)
        frequency = 25  # 25 Hz
        amplitude = 1.0
        noise_level = 0.1

        # Create synthetic seismic trace
        signal = amplitude * np.sin(2 * np.pi * frequency * time)
        noise = noise_level * np.random.randn(len(time))
        data = signal + noise

        # Initialize components
        print("Initializing components...")
        extractor = FeatureExtractor()
        controller = QualityController()
        plotter = SeismicPlotter()

        # Extract features
        print("Extracting features...")
        features = extractor.extract_features(data)
        print("\nExtracted Features:")
        for category, values in features.items():
            if isinstance(values, dict):
                print(f"\n{category.upper()}:")
                for key, value in values.items():
                    print(f"  {key}: {value}")
            else:
                print(f"\n{category.upper()}: {values}")

        # Perform quality control
        print("\nPerforming quality control...")
        qc_results = controller.quality_check(data)
        print("\nQuality Control Results:")
        for category, values in qc_results.items():
            if isinstance(values, dict):
                print(f"\n{category.upper()}:")
                for key, value in values.items():
                    print(f"  {key}: {value}")
            else:
                print(f"\n{category.upper()}: {values}")

        # Create output directory if it doesn't exist
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        print("\nGenerating visualizations...")
        # Create visualizations
        plotter.plot_seismic_trace(
            data, 
            sample_rate, 
            save_path=os.path.join(output_dir, "seismic_trace.png")
        )
        plotter.plot_frequency_spectrum(
            data, 
            sample_rate, 
            save_path=os.path.join(output_dir, "frequency_spectrum.png")
        )
        plotter.plot_qc_results(
            qc_results, 
            save_path=os.path.join(output_dir, "qc_results.png")
        )

        print("\nVisualizations saved in 'output' directory:")
        print("- seismic_trace.png")
        print("- frequency_spectrum.png")
        print("- qc_results.png")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
