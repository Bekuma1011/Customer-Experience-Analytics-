import pandas as pd
from datetime import datetime
import os

class ReviewPreprocessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        print("Loading data...")
        self.df = pd.read_csv(self.input_path)

    def clean_data(self):
        print("Cleaning data...")
        self.df.drop_duplicates(subset=["review", "rating", "date", "bank"], inplace=True)
        self.df.dropna(subset=["review", "rating", "date", "bank"], inplace=True)
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.strftime('%Y-%m-%d')

    def save_cleaned_data(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        print(f"Cleaned data saved to {self.output_path}")

    def show_stats(self):
        print("\n Review counts per bank:")
        print(self.df["bank"].value_counts())


