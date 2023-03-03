import pandas as pd
import os

fun_decision = True


# Funkcja do wczytywania wszystkich ramek będących w folderze
def load_csv():
    path = os.path.dirname(__file__)
    extension = ".csv"

    # lista nazw plików bez rozszerzenia
    files = [file[:-len(extension)] for file in os.listdir(path) if file.endswith(extension)]

    # pętla wczytująca pliki i tworząca ramki danych
    for file in files:
        # wczytanie pliku csv
        csv_file = os.path.join(path, file + extension)
        if os.path.isfile(csv_file):
            if '.' in pd.read_csv(csv_file, sep=';', encoding='utf-8', decimal='.').columns.tolist():
                decimal = '.'
            else:
                decimal = ','
            df_name = "df_" + file.lower()
            globals()[df_name] = pd.read_csv(csv_file, sep=";", encoding='utf-8', decimal=decimal)
            print(f"Utworzono ramkę danych {df_name} z pliku {file}.csv")


def data_frames():
    print("Utworzone ramki danych:")
    for var in globals():
        if isinstance(globals()[var], pd.core.frame.DataFrame):
            print(var)
            print(f'{globals()[var]}\n')
