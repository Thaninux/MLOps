import os
import pandas as pd

def preprocess(input_path: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path, sep=";", parse_dates={"datetime": [0, 1]}, dayfirst=True)
    df["hour"] = df["datetime"].dt.hour
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess("data/household_power_consumption.txt", "data/processed/power_2008.csv")