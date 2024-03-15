import pandas as pd


def load_and_view_data(file_path):
    df = pd.read_csv(file_path)
    print("Erste fünf Zeilen des Datensatzes:")
    print(df.head())
    return df
