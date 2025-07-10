# Contents of /intrusion-detection-system-ml/intrusion-detection-system-ml/src/model_training.py

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
import joblib

class ModelTrainer:
    def __init__(self, data, model=None):
        self.data = data
        self.model = model if model else IsolationForest()

    def preprocess_data(self):
        # Assuming the last column is the target variable
        X = self.data.iloc[:, :-1]
        y = self.data.iloc[:, -1]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def fit(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train)
        return self.model.score(X_test, y_test)

    def save_model(self, filename):
        joblib.dump(self.model, filename)

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('path_to_your_dataset.csv')  # Replace with your dataset path
    trainer = ModelTrainer(data)
    accuracy = trainer.fit()
    print(f"Model accuracy: {accuracy}")
    trainer.save_model('trained_model.pkl')