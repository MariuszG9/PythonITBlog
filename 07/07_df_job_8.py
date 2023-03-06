import pandas as pd
import os
from prettytable import PrettyTable
import numpy as np

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
            decimal = ',' if pd.read_csv(csv_file, sep=';', encoding='utf-8', nrows=1).iloc[0].str.contains(',').any() else '.'
            df_name = "df_" + file.lower()
            globals()[df_name] = pd.read_csv(csv_file, sep=";", encoding='utf-8', decimal=decimal)
            print(f"Utworzono ramkę danych {df_name} z pliku {file}.csv")


def data_frames():
    print("Utworzone ramki danych:")
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            print(var)
            print(f'{globals()[var]}\n')


def pretty_info():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            df = globals()[var]
            table = PrettyTable()
            null_count = df.isnull().sum().sum()
            nan_count = df.isna().sum().sum()
            table.field_names = [''] + list(df.describe(include='all').columns)
            for i, row in enumerate(df.describe(include='all').itertuples()):
                table.add_row([f"{row[0]}"] + [f"{x:.2f}" if isinstance(x, (int, float)) else x for x in row[1:]])
            print(table)
            print(f"Liczba duplikatów: {df.duplicated().sum()}")
            print(f"Liczba wartości: NULL = {null_count} |  NaN: {nan_count}\n")


def delete_duplicates():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            df = globals()[var]
            df.drop_duplicates(inplace=True)
            print(f"Usunięto duplikaty z ramki danych {var}")
    pretty_info()


def delete_nulls():
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            print(f"DataFrame: {var}")
            globals()[var] = globals()[var].dropna()
    pretty_info()


while fun_decision:
    select = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]"
                       f"\n🔹Wypisanie ramek danych [2]\n🔹Informacje o ramkach [3]\n🔹Usuń duplikaty [4]"
                       f"\n🔹Usuń rekordy z NULL'ami [5]\n"
                       f"\ndecyzja: "))
    if select == 1:
        load_csv()
    elif select == 2:
        data_frames()
    elif select == 3:
        pretty_info()
    elif select == 4:
        delete_duplicates()
    elif select == 5:
        delete_nulls()
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


