import pandas as pd

def load_data(data_path):
    try:
        data = pd.read_csv(data_path)
        return data
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_path}")
        return None

def clean_data(data):
    data = data.dropna()
    # Ensure numeric columns are of the correct type
    data['n_trials'] = pd.to_numeric(data['n_trials'], errors='coerce')
    data['n_conversions'] = pd.to_numeric(data['n_conversions'], errors='coerce')
    return data

def prepare_data(data_path):
    data = load_data(data_path)
    if data is not None:
        data = clean_data(data)
    return data

if __name__ == "__main__":
    data = prepare_data("data/ab_test.csv")
    if data is not None:
        print(data.head())
        print(data.info())
