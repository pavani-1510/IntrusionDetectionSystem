# Data Preprocessing Module for Anomaly-Based Intrusion Detection System

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load dataset from a specified file path."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the dataset by handling missing values and duplicates."""
    data = data.drop_duplicates()
    data = data.fillna(method='ffill')  # Forward fill for missing values
    return data

def normalize_data(data):
    """Normalize the dataset using StandardScaler."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Split the dataset into training and testing sets."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def save_csv(X_train, y_train, target_column):
    processed_data = pd.DataFrame(X_train_scaled, columns=X_train.columns)
    processed_data[target_column] = y_train.reset_index(drop=True)
    processed_data.to_csv("processed_data.csv", index=False)
    print("Processed data saved to 'processed_data.csv'")

if __name__ == "__main__":
    # Example usage
    file_path = "/home/pavani/Documents/VSCODE/IntrusionDetectionSystem/packets.csv"  # Update with your actual file path

    data = load_data(file_path)
    print("Original data shape:", data.shape)
    print("Columns:", data.columns.tolist())  # <-- Add this line

    data = clean_data(data)
    print("After cleaning:", data.shape)
    print("Columns after cleaning:", data.columns.tolist())  
    target_column = "ip.proto"  

    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in data columns: {data.columns.tolist()}")

    X_train, X_test, y_train, y_test = split_data(data, target_column)
    print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

    # Normalize features (excluding target)
    X_train_scaled = normalize_data(X_train)
    X_test_scaled = normalize_data(X_test)
    print("Normalized train shape:", X_train_scaled.shape, "Normalized test shape:", X_test_scaled.shape)
    save_csv(X_train_scaled, y_train, target_column)
