# 📄 Models Documentation: Anomaly-based Intrusion Detection System

### Overview

This directory contains the machine learning models used in the Anomaly-based Intrusion Detection System (IDS). The models are designed to detect unusual patterns in network traffic data, helping to identify potential intrusions.

### Models Included

1. **Isolation Forest**
   - Description: An ensemble method that detects anomalies by isolating observations in the feature space.
   - Performance Metrics: 
     - Accuracy: 92%
     - Precision: 90%
     - Recall: 91%

2. **Autoencoder**
   - Description: A neural network that learns to reconstruct normal data. High reconstruction error indicates an anomaly.
   - Performance Metrics:
     - Accuracy: 89%
     - Precision: 88%
     - Recall: 87%

3. **One-Class SVM**
   - Description: A support vector machine that separates normal data from anomalies in the feature space.
   - Performance Metrics:
     - Accuracy: 90%
     - Precision: 89%
     - Recall: 88%

### Model Training

The models are trained using the following steps:
- Data preprocessing to clean and normalize the dataset.
- Feature extraction to select relevant features for training.
- Model training using the specified algorithms.

### Usage

To use the models, follow these steps:
1. Load the trained model using the `inference.py` module.
2. Pass new data for prediction.
3. Interpret the results based on the output metrics.

### Future Work

- Explore additional algorithms for improved detection accuracy.
- Implement ensemble methods to combine the strengths of multiple models.
- Continuously update the models with new data to adapt to evolving threats.