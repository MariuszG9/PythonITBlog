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


def remove_column():
    # Wypisz dostępne ramki danych
    data_frames_list = []
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            data_frames_list.append(var)
    if not data_frames_list:
        print("Brak dostępnych ramek danych.")
        return
    print("Dostępne ramki danych:")
    x = PrettyTable()
    x.field_names = ["#", "Nazwa ramki danych"]
    for i, name in enumerate(data_frames_list):
        x.add_row([i+1, name])
    print(x)

    # Wybierz ramkę danych do modyfikacji
    while True:
        try:
            df_name = data_frames_list[int(input("Podaj numer ramki danych do modyfikacji: ")) - 1]
            df = globals()[df_name]
            break
        except (IndexError, ValueError):
            print("Niepoprawny numer ramki danych.")

    # Wypisz nazwy kolumn wraz z ich numerami
    print(f"Dostępne kolumny w ramce danych '{df_name}':")
    x = PrettyTable()
    x.field_names = ["#", "Nazwa kolumny"]
    for i, col_name in enumerate(df.columns):
        x.add_row([i+1, col_name])
    print(x)

    # Wybierz kolumnę do usunięcia
    while True:
        try:
            choice = input("Podaj nazwę lub numer kolumny do usunięcia: ")
            if choice.isdigit():
                col_num = int(choice) - 1
                col_name = df.columns[col_num]
            else:
                col_name = choice
                col_num = df.columns.get_loc(col_name)
            break
        except (IndexError, ValueError):
            print("Niepoprawna nazwa lub numer kolumny.")

    # Usuń kolumnę z ramki danych
    df.drop(df.columns[col_num], axis=1, inplace=True)
    print(f"Usunięto kolumnę '{col_name}' z ramki danych '{df_name}'.")


def rename_column():
    # Wydruk dostępnych ramek
    print("Dostępne ramki danych:")
    dataframes = []
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            dataframes.append(var)
    table = PrettyTable()
    table.field_names = ["Numer", "Nazwa"]
    for i, df in enumerate(dataframes):
        table.add_row([i, df])
    print(table)

    # Uzyskujemy informacje która ramka i kolumn
    df_choice = int(input("Wybierz numer ramki danych: "))
    df_name = dataframes[df_choice]
    df = globals()[df_name]
    columns = df.columns.tolist()
    table = PrettyTable()
    table.field_names = ["Numer", "Nazwa kolumny"]
    for i, col in enumerate(columns):
        table.add_row([i, col])
    print(table)
    col_choice = int(input("Wybierz numer kolumny, którą chcesz zmienić nazwę: "))
    old_col_name = columns[col_choice]

    # Zapytamy o nazwę nowej kolumny
    new_col_name = input("Podaj nową nazwę dla kolumny: ")

    # zmieniamy nazwę kolumny
    df.rename(columns={old_col_name: new_col_name}, inplace=True)

    # Drukujemy nagłówek z ramki
    print(f"\nKolumna {old_col_name} w ramce danych {df_name} zmieniła nazwę na {new_col_name}.\n")
    print(df.head())

    # Aktualizujemy globalną zmienną df
    globals()[df_name] = df


while fun_decision:
    select = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]"
                       f"\n🔹Wypisanie ramek danych [2]\n🔹Informacje o ramkach [3]\n🔹Usuń duplikaty [4]"
                       f"\n🔹Usuń rekordy z NULL'ami [5]\n🔹Usuń kolumny [6]\n🔹Zmień nazwę kolumny [7]"
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
    elif select == 6:
        remove_column()
    elif select == 7:
        rename_column()
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


