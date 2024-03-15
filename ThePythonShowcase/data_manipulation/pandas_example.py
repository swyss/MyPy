import pandas as pd


# Funktion zum Laden und Anzeigen von Daten
def load_and_view_data(file_path):
    df = pd.read_csv(file_path)
    print("Erste fünf Zeilen des Datensatzes:")
    print(df.head())
    return df


# Funktion zur Datenbereinigung
def clean_data(df):
    # Einfache Bereinigung: Entferne Zeilen mit fehlenden Werten
    df_clean = df.dropna()
    print("\nDaten nach der Bereinigung:")
    print(df_clean.info())
    return df_clean


# Funktion zur Datentransformation
def transform_data(df):
    # Beispieltransformation: Gruppierung nach einer Spalte und Berechnung des Durchschnitts
    if 'Kategorie' in df.columns:  # Ersetze 'Kategorie' durch einen tatsächlichen Spaltennamen deiner Wahl
        grouped_df = df.groupby('Kategorie').mean()
        print("\nDaten nach der Transformation (Gruppierung und Durchschnitt):")
        print(grouped_df.head())
    else:
        print("\n'Die Spalte 'Kategorie' existiert nicht im DataFrame.")
        grouped_df = df
    return grouped_df


# Funktion für einfache Datenanalyse
def analyze_data(df):
    print("\nDeskriptive Statistik des Datensatzes:")
    print(df.describe())


# Hauptfunktion, die alles zusammenführt
def main():
    file_path = 'path/to/your/data.csv'  # Ersetze dies durch den tatsächlichen Pfad zu deinem CSV-Datensatz

    # Daten laden und anzeigen
    df = load_and_view_data(file_path)

    # Daten bereinigen
    df_clean = clean_data(df)

    # Daten transformieren
    df_transformed = transform_data(df_clean)

    # Datenanalyse durchführen
    analyze_data(df_transformed)


if __name__ == "__main__":
    main()
