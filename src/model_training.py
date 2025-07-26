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
        df = self.data.copy()

        # Convert timestamp columns to numeric if present
        for col in df.columns:
            if 'time' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce').astype('int64')
                except Exception:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

        # One-hot encode categorical columns (except the target)
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X = pd.get_dummies(X)

        # Keep only numeric columns
        X = X.select_dtypes(include=['number'])
        if X.shape[1] == 0:
            raise ValueError("No numeric columns found in the dataset for model training.")
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def fit(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train)
        # Predict on test set
        y_pred = self.model.predict(X_test)
        # If your y_test labels are not -1/1, map them accordingly
        y_test_mapped = y_test.copy()
        if not set(y_test.unique()).issubset({-1, 1}):
            # Try to map the most frequent value to 1 (normal), others to -1 (anomaly)
            most_common = y_test.value_counts().idxmax()
            y_test_mapped = y_test.apply(lambda x: 1 if x == most_common else -1)
        accuracy = (y_pred == y_test_mapped).mean()
        return accuracy

    def save_model(self, filename):
        joblib.dump(self.model, filename)

if __name__ == "__main__":
    data = pd.read_csv('../data/packets.csv')  # Use relative path
    trainer = ModelTrainer(data)
    accuracy = trainer.fit()
    print(f"✅ Model trained with accuracy: {accuracy:.2f}")
    trainer.save_model('../models/trained_model.pkl')
    print("🎉 Model saved to '../models/trained_model.pkl'")
