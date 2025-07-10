# Contents of /intrusion-detection-system-ml/intrusion-detection-system-ml/src/inference.py

import joblib
import pandas as pd

def load_model(model_path):
    """Load the trained machine learning model from the specified path."""
    model = joblib.load(model_path)
    return model

def make_prediction(model, data):
    """Make predictions using the loaded model on the provided data."""
    predictions = model.predict(data)
    return predictions

def interpret_results(predictions):
    """Interpret the prediction results and return a human-readable format."""
    results = ["Anomaly" if pred == 1 else "Normal" for pred in predictions]
    return results

def run_inference(model_path, input_data):
    """Load the model and make predictions on the input data."""
    model = load_model(model_path)
    predictions = make_prediction(model, input_data)
    interpreted_results = interpret_results(predictions)
    return interpreted_results