import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import kagglehub

def download_kaggle_dataset():
    """Download dataset using kagglehub."""
    try:
        path = kagglehub.dataset_download("kaggleprollc/nsl-kdd99-dataset")
        print("Dataset downloaded to:", path)
        return path
    except Exception as e:
        print("Failed to download dataset:", e)
        return None

def find_supported_file(dataset_dir, tried_files=None):
    """Find the next supported file in the dataset directory, skipping files that failed."""
    files = os.listdir(dataset_dir)
    if tried_files is None:
        tried_files = set()
    for f in files:
        if f.lower().endswith(('.csv', '.xlsx', '.json', '.arff', '.txt')) and f not in tried_files:
            return os.path.join(dataset_dir, f)
    return None

def load_data(file_path):
    """Load dataset from a specified file path."""
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == '.csv':
            return pd.read_csv(file_path)
        elif ext == '.xlsx':
            return pd.read_excel(file_path)
        elif ext == '.json':
            return pd.read_json(file_path)
        elif ext == '.arff':
            from scipy.io import arff
            arff_data, _ = arff.loadarff(file_path)
            df = pd.DataFrame(arff_data)
            for col in df.select_dtypes([object]).columns:
                df[col] = df[col].apply(lambda x: x.decode('utf-8').strip() if isinstance(x, bytes) else x)
            return df
        elif ext == '.txt':
            return pd.read_csv(file_path, sep=None, engine='python')
        else:
            print(f"Unsupported file format: {ext}")
            return None
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def clean_data(data):
    """Clean the dataset by handling missing values and duplicates."""
    data = data.drop_duplicates()
    data = data.fillna(method='ffill')
    return data

def preprocess_features(X):
    """Convert categorical columns to numeric using one-hot encoding."""
    X_numeric = pd.get_dummies(X)
    dropped = set(X.columns) - set(X_numeric.columns)
    if dropped:
        print(f"Warning: Dropped non-numeric columns: {dropped}")
    return X_numeric

def normalize_data(data):
    """Normalize the dataset using StandardScaler."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Split the dataset into training and testing sets."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def save_csv(X_train_scaled, y_train, target_column):
    """Save the preprocessed training data to CSV."""
    processed_data = X_train_scaled.copy()
    processed_data[target_column] = y_train.reset_index(drop=True)
    dataset_dir = os.path.join(os.path.dirname(__file__), '../dataset')
    os.makedirs(dataset_dir, exist_ok=True)
    processed_csv = os.path.join(dataset_dir, "processed_data.csv")
    processed_data.to_csv(processed_csv, index=False)
    print(f"Processed data saved to '{processed_csv}'")

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__), '../dataset')

    # Step 1: Download dataset
    dataset_path = download_kaggle_dataset()
    if dataset_path:
        base_dir = dataset_path

    tried_files = set()
    file_path = find_supported_file(base_dir)
    data = None

    # Step 2: Try to load data
    while file_path:
        print(f"Trying file: {file_path}")
        data = load_data(file_path)
        if data is not None and not data.empty:
            break
        tried_files.add(os.path.basename(file_path))
        file_path = find_supported_file(base_dir, tried_files)

    if data is None or data.empty:
        print("No valid data file found.")
        exit(1)

    print("Original Data Shape:", data.shape)
    print("Columns:", data.columns.tolist())

    # Step 3: Auto-detect target column
    possible_targets = ['label', 'ip.proto', 'target', 'class']
    target_column = next((col for col in possible_targets if col in data.columns), None)

    if not target_column:
        last_col = data.columns[-1]
        if data[last_col].nunique() < max(20, data.shape[0] // 100):
            target_column = last_col
            print(f"Auto-detected target column: '{target_column}'")
        else:
            print("Could not determine target column. Please rename the label column appropriately.")
            exit(1)

    # Step 4: Preprocess
    data = clean_data(data)
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in data.")

    X_train, X_test, y_train, y_test = split_data(data, target_column)
    print("Train/Test shapes:", X_train.shape, X_test.shape)

    X_train_numeric = preprocess_features(X_train)
    X_test_numeric = preprocess_features(X_test)

    X_train_scaled = normalize_data(X_train_numeric)
    X_test_scaled = normalize_data(X_test_numeric)

    print("Scaled train shape:", X_train_scaled.shape, "Scaled test shape:", X_test_scaled.shape)

    save_csv(X_train_scaled, y_train, target_column)
