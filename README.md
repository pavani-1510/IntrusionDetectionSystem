# 🛡️ Intrusion Detection System using Machine Learning

An **Anomaly-Based Intrusion Detection System (IDS)** that downloads a dataset, preprocesses it, trains a machine learning model, and displays a visual dashboard to monitor intrusions. Built using Python and the Isolation Forest algorithm.

---

### 🚀 How It Works

1. **`data_preprocessing.py`**: Downloads and preprocesses the dataset.
2. **`model_training.py`**: Trains a machine learning model using the preprocessed data.
3. **`dashboard.py`**: Launches a simple dashboard to show predictions or system status.

---

### 📁 Project Structure

```
IntrusionDetectionSystem/
│
├── src/
│   ├── data_preprocessing.py       # Download + clean + prepare dataset
│   ├── model_training.py           # Trains and saves the ML model
│   └── dashboard.py                # Launches monitoring dashboard
│   
│
├── models/
│   └── isolation_forest_model.pkl  # Trained model (saved here)
│
├── data/
│   └── dataset.csv                 # Auto-downloaded dataset
│
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

### ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/IntrusionDetectionSystem.git
   cd IntrusionDetectionSystem
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

### 🧪 Usage

#### 1. Run Data Preprocessing

This script downloads and processes the dataset into `data/processed.csv`.

```bash
python src/data_preprocessing.py
```

#### 2. Train the Model

Trains an Isolation Forest model and saves it to `models/`.

```bash
python src/model_training.py
```

#### 3. Launch the Dashboard

Starts a GUI or web-based dashboard to view predictions or stats.

```bash
python src/dashboard.py
```

> ⚠️ Make sure `model_training.py` has completed successfully before launching the dashboard.

---

### 💡 Features

* Automatic dataset fetching and cleaning
* Isolation Forest for anomaly detection
* Modular and easy-to-extend pipeline
* (Optional) Dashboard to monitor intrusions visually

---

### 🧠 Model Used

* **Isolation Forest** (unsupervised anomaly detection)

---

### ✅ Future Enhancements

* [ ] Add support for live network traffic via Scapy
* [ ] Improve dashboard UI (e.g., Streamlit or Flask)
* [ ] Add logs/alerts when intrusions are detected
* [ ] Save metrics and generate ROC/PR curves

---

### 📄 License

Licensed under the MIT License – feel free to use, modify, and share.

---

### 👩‍💻 Author

**Pavani R**
B.Tech CSE | AI/ML | Cybersecurity Enthusiast
📫 [pavanikangundi@gmail.com](mailto:pavanikangundi@gmail.com) 
🔗 [LinkedIn](https://www.linkedin.com/in/r-pavani)
