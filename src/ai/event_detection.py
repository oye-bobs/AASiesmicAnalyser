import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class SeismicEventDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        
    def train(self, X: np.ndarray, y: np.ndarray):
        """Train the model with seismic data."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict seismic events from new data."""
        return self.model.predict(X)
