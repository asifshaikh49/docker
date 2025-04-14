import pandas as pd
import os

# Dynamically get path relative to script location
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, 'data', 'data.csv')

try:
    # Read the CSV file
    df = pd.read_csv(csv_path)
    print("\n Data Loaded Successfully!\n")
    
    # Print basic statistics
    print(df.describe())
except FileNotFoundError:
    print(f" Error: File not found at {csv_path}")
except pd.errors.EmptyDataError:
    print(" Error: CSV file is empty.")
except Exception as e:
    print(f" Unexpected Error: {e}")

