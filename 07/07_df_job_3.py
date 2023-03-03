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
            if '.' in pd.read_csv(csv_file, nrows=1, sep=';', encoding='utf-8', decimal='.').columns.tolist():
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


while fun_decision:
    select = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]\n🔹Wypisanie ramek danych [2]"
                       f"\ndecyzja: "))
    if select == 1:
        load_csv()
    elif select == 2:
        data_frames()
    else:
        print("Źle wybrano")

    decision = None
    while decision != 'T' and decision != 'N':
        decision = input("Nie wybrano żadnej funkcji. Czy chcesz wybrać jeszcze raz? [N/T]: ").upper()
        if decision == 'T':
            fun_decision = True
        elif decision == 'N':
            fun_decision = False
        else:
            print("Jeszcze raz")
