import pandas as pd
import os
from prettytable import PrettyTable

fun_decision = True
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)

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
    for var in list(globals()):
        if isinstance(globals()[var], pd.DataFrame):
            print(var)
            print(f'{globals()[var]}\n')


def pretty_info():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            df = globals()[var]
            table = PrettyTable()
            table.field_names = [''] + list(df.describe(include='all').columns)
            for i, row in enumerate(df.describe(include='all').itertuples()):
                table.add_row([f"{row[0]}"] + [f"{x:.2f}" if isinstance(x, (int, float)) else x for x in row[1:]])
            print(table)


while fun_decision:
    select = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]\n🔹Wypisanie ramek danych [2]"
                       f"\ndecyzja: "))
    if select == 1:
        load_csv()
    elif select == 2:
        data_frames()
    elif select == 3:
        pretty_info()
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
