import pytest
import numpy as np
from src.ai.event_detection import SeismicEventDetector

def test_event_detector():
    detector = SeismicEventDetector()
    X = np.random.randn(1000, 10)
    y = np.random.randint(0, 2, 1000)
    detector.train(X, y)
    X_new = np.random.randn(10, 10)
    predictions = detector.predict(X_new)
    assert len(predictions) == 10
