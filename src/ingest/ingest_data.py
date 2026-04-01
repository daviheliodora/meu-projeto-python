import pandas as pd
import os

def read_csv(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    data = pd.read_csv(file_path)
    validate_data(data)
    return data

def validate_data(data):
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")
