import numpy as np
from src.ai.event_detection import SeismicEventDetector

# Generate some synthetic data for demonstration purposes
# In practice, you would load your seismic data and labels here
X = np.random.randn(1000, 10)  # 1000 samples, 10 features each
y = np.random.randint(0, 2, 1000)  # Binary labels (0 or 1)

# Initialize and train the detector
detector = SeismicEventDetector()
detector.train(X, y)

# Predict on new data
X_new = np.random.randn(10, 10)  # 10 new samples
predictions = detector.predict(X_new)
print("Predictions:", predictions)
