# 📄 Dataset Documentation for Anomaly-based Intrusion Detection System

## Overview

This directory contains datasets used for training and evaluating the anomaly-based Intrusion Detection System (IDS) built using machine learning techniques. The datasets are crucial for developing a robust model that can accurately detect anomalies in network traffic.

## Datasets

### 1. NSL-KDD

- **Description**: The NSL-KDD dataset is a refined version of the original KDD'99 dataset. It addresses some of the inherent problems of the KDD'99 dataset, such as redundant records and imbalanced class distribution.
- **Usage**: Recommended for beginners due to its smaller size and cleaned nature.
- **Download Link**: [NSL-KDD Dataset](http://www.unb.ca/cic/datasets/nsl.html)

### 2. CICIDS2017

- **Description**: The CICIDS2017 dataset is a large and realistic dataset that includes modern attack scenarios. It provides a comprehensive set of features for various types of attacks.
- **Usage**: Suitable for advanced users looking for a more challenging dataset with realistic traffic patterns.
- **Download Link**: [CICIDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)

## Instructions for Downloading

1. Visit the provided links for each dataset.
2. Follow the instructions on the respective pages to download the datasets.
3. Place the downloaded files in the `data` directory of the project for easy access during data preprocessing and model training.

## Data Format

The datasets are typically provided in CSV format, which can be easily loaded using pandas in Python. Ensure that the data is cleaned and preprocessed before feeding it into the machine learning model.

## Acknowledgments

We acknowledge the creators of the NSL-KDD and CICIDS2017 datasets for their contributions to the field of network security and anomaly detection.