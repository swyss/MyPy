from loading_and_viewing_data import load_and_view_data
from data_cleaning import clean_data
from data_transformation import transform_data
from data_analysis import analyze_data


def main():
    file_path = 'path/to/your/data.csv'  # Ersetze dies durch den tatsächlichen Pfad zu deinem CSV-Datensatz

    # Daten laden und anzeigen
    df = load_and_view_data(file_path)

    # Daten bereinigen
    df_clean = clean_data(df)

    # Daten transformieren
    df_transformed = transform_data(df_clean,
                                    column_name='DeineSpaltenbezeichnung')  # Ersetze 'DeineSpaltenbezeichnung'

    # Datenanalyse durchführen
    analyze_data(df_transformed)


if __name__ == "__main__":
    main()
