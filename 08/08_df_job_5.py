import pandas as pd
import os
from prettytable import PrettyTable
import json
import pyodbc
import logging


fun_decision = True
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)


# Funkcja do wczytywania wszystkich ramek będących w folderze
def load_csv():
    path = os.path.dirname(__file__)
    extension = ".csv"
    df_list = []

    # lista nazw plików bez rozszerzenia
    files = [file[:-len(extension)] for file in os.listdir(path) if file.endswith(extension)]

    # pętla wczytująca pliki i tworząca ramki danych
    for file in files:
        # wczytanie pliku csv
        csv_file = os.path.join(path, file + extension)
        if os.path.isfile(csv_file):
            decimal = ',' if pd.read_csv(csv_file, sep=';', encoding='utf-8', nrows=1).iloc[0].str.contains(',').any() else '.'
            df_name = "df_" + file.lower()
            df_list.append(file)
            globals()[df_name] = pd.read_csv(csv_file, sep=";", encoding='utf-8', decimal=decimal)
            print(f"Utworzono ramkę danych {df_name} z pliku {file}.csv")
    data_frame_operation(f"wczytano ramkę danych {df_list}")


def data_frames():
    df_list = []
    print("Utworzone ramki danych:")
    for var in globals():

        if isinstance(globals()[var], pd.DataFrame):
            print(var)
            print(f'{globals()[var]}\n')
            df_list.append(var)
    data_frame_operation(f"Wypisano ramki {df_list}")


def pretty_info():
    df_list = []
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
            df_list.append(var)
    data_frame_operation(f"Wypisano statystyki dla ramek {df_list}")


def delete_duplicates():
    duplicates_removed = []
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            df = globals()[var]
            n_before = len(df)
            df.drop_duplicates(inplace=True)
            n_after = len(df)
            if n_before != n_after:
                duplicates_removed.append((var, n_before - n_after))
                print(f"Usunięto {n_before - n_after} duplikaty z ramki danych {var}")
    pretty_info()
    data_frame_operation(f"Usunięto duplikaty, ilość: {duplicates_removed}")


def delete_nulls():
    nulls_removed = 0
    null_invoices = []
    for var in globals():
        if isinstance(globals()[var], pd.DataFrame):
            print(f"DataFrame: {var}")
            df = globals()[var]
            null_count = df.isnull().sum().sum()
            nulls_removed += null_count
            if null_count > 0:
                null_invoices.extend(df.loc[df.isnull().any(axis=1), 'invoice_num'].tolist())
            globals()[var] = df.dropna()
    pretty_info()
    if nulls_removed > 0:
        print(f"Usunięto {nulls_removed} wartości NULL z ramki danych.")
        if null_invoices:
            print(f"Numery faktur, które zawierały wartości NULL: {', '.join(str(inv) for inv in null_invoices)}")
    else:
        print("Nie znaleziono wartości NULL w ramkach danych.")
    data_frame_operation(f"Usunięto wartości NULL z ramki danych. FV: {', '.join(str(inv) for inv in null_invoices)}")


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
    data_frame_operation(f"Usunięto kolumnę {col_name} z ramki danych '{df_name}")


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

    while True:
        try:
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
            break
        except ValueError:
            print("Podano nieprawidłową wartość. Wybierz liczbę z przedziału [0, {}]".format(len(dataframes) - 1))
        except IndexError:
            print("Podano nieprawidłowy numer ramki danych. Wybierz liczbę z przedziału [0, {}]".format(len(dataframes) - 1))
        except:
            print("Wystąpił nieznany błąd. Spróbuj ponownie.")

    # Zapytamy o nazwę nowej kolumny
    new_col_name = input("Podaj nową nazwę dla kolumny: ")

    # zmieniamy nazwę kolumny
    df.rename(columns={old_col_name: new_col_name}, inplace=True)

    # Drukujemy nagłówek z ramki
    print(f"\nKolumna {old_col_name} w ramce danych {df_name} zmieniła nazwę na {new_col_name}.\n")
    print(df.head())

    # Aktualizujemy globalną zmienną df
    globals()[df_name] = df
    data_frame_operation(f"Kolumna {old_col_name} w ramce danych {df_name} zmieniła nazwę na {new_col_name}")


def concat_dataframes():
    mask = 'df_sales_'
    dfs = [v for k, v in globals().items() if k.startswith(mask)]
    merged_df = pd.concat(dfs)
    globals()['merged_df'] = merged_df
    print(merged_df)
    df_names = ', '.join([k for k, v in globals().items() if k.startswith(mask)])
    data_frame_operation(f"Połączono ramki danych: {df_names}")


def merge_dataframes():
    merged_df = globals()['merged_df']
    df_salesman = globals()['df_salesman']
    merged_df_with_salesman = pd.merge(merged_df, df_salesman[['salesman_id', 'surname']], on='salesman_id', how='left')
    globals()['merged_df_with_salesman'] = merged_df_with_salesman
    print(merged_df_with_salesman)
    data_frame_operation(f"Dołączono ramkę danych df_salesman")


def create_columns():
    merged_df_ws = globals()['merged_df_with_salesman']
    merged_df_ws['value_up'] = merged_df_ws['value'] * 1.08

    # Obliczenie kolumny "rebate_value"
    merged_df_ws['rebate_value'] = merged_df_ws['value']
    merged_df_ws.loc[merged_df_ws['quantity'] > 10000, 'rebate_value'] *= 0.9

    # Obliczenie kolumny "price_per_unit"
    merged_df_ws['price_per_unit'] = 0
    mask = merged_df_ws['quantity'] != 0
    merged_df_ws.loc[mask, 'price_per_unit'] = merged_df_ws.loc[mask, 'value'] / \
                                               merged_df_ws.loc[mask, 'quantity']
    globals()['merged_df_database'] = merged_df_ws
    print(merged_df_ws)
    data_frame_operation(f"Utworzono kolumny: value_up, reabte_value oraz price_per_unit")


def load_frame():
    table_data = []
    table_name = 'sales_per_country'
    server_connect = None

    with open('server_config.json') as frm:
        datajson = json.load(frm)

    print(f'Możliwe konfiguracje serwera: \n🔹0-testowy\n🔹1-produkcyjny')

    # Konfiguracja wyboru środowiska
    server_number = int(input('Podaj cyfrę:'))
    server = datajson['servers']
    if server_number == 0:
        server_connect = server[0]
        print(server_connect)
    elif server_number == 1:
        server_connect = server[1]
    else:
        print("zły profil")

    driver_j = server_connect['DRIVER']
    server_j = server_connect['SERVER']
    database_j = server_connect['DATABASE']

    # Ustawienie parametrów logowania z pliku JSON
    conn = pyodbc.connect('driver='+driver_j+';'
                          'server='+server_j+';'
                          'database='+database_j+';'
                         'Trusted_Connection=yes')
    cursor = conn.cursor()
    print(f'Zostałeś prawidłowo połączony z {server_j}, {database_j}')

    # Try...except obsługujący pobranie danych CSV do aplikacji
    try:
        df = globals()['merged_df_database']
        print(df)
        df["invoice_num"] = df['invoice_num'].astype('object')
        df["salesman_id"] = df['salesman_id'].astype(str)
        df["market"] = df['market'].astype(str)
        df["quantity"] = df['quantity'].astype(float)
        df["value"] = df['value'].astype(float)
        df["customer"] = df['customer'].astype('object')
        df["fv_date"] = pd.to_datetime(df['fv_date'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')
        df["surname"] = df['surname'].astype(str)
        df["value_up"] = df['value_up'].astype(float)
        df["rebate_value"] = df['rebate_value'].astype(float)
    except Exception as exc:
        print('⚠ Nie utworzyłeś jeszcze ramki danych, która spełniałaby wymagania')
        raise exc

    # Try...except dla operacji na bazie danych.
    try:
        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()
        for index, row in df.iterrows():
            row = list(row)
            sql_query = f"""INSERT INTO {table_name} (invoice_number, salesman_id, market, quantity, value, customer, 
            fv_date, surname, value_up, rebate_value) VALUES (?,?,?,?,?,?,?,?,?,?)"""
            cursor.execute(sql_query, row)
            conn.commit()
    except Exception as exc:
        print('⚠ Nie zapisano danych')
        upload_data_error(table_name, table_data)
        raise exc

    print('✔ Dane commission zostały zaktualizowane poprawnie')
    upload_data_correctly(table_name, table_data)
    conn.close()


def setup_logging(log_file):
    # Tworzenie obiektu loggera
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Tworzenie obiektu obsługującego zapisywanie logów do pliku
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    # Ustawienie formatu logów
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


# Funkcja do zwracania wyniku próby jako negatywnego
def upload_data_error(table_name, date):
    logger.info(f"Nie wgrano danych do tabeli {table_name}")


# Funkcja do zwracania wyniku próby jako pozytywnego
def upload_data_correctly(table_name, date):
    logger.info(f"Wgrano dane do tabeli {table_name} | Dane zostały zrzucone i załadowane ponownie")


# Funkcja do zwracania wyniku próby jako pozytywnego
def data_frame_operation(type_of):
    logger.info(f"Wykonano: {type_of}")


logger = setup_logging('plik_logow.txt')

while fun_decision:
    selected_option = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]"
                       f"\n🔹Wypisanie ramek danych [2]\n🔹Informacje o ramkach [3]\n🔹Usuń duplikaty [4]"
                       f"\n🔹Usuń rekordy z NULL'ami [5]\n🔹Usuń kolumny [6]\n🔹Zmień nazwę kolumny [7]"
                       f"\n🔹Połącz ramki o masce df_salesman_* [8]\n🔹Dołącz tabelę Salesman [9]"
                       f"\n🔹Utwórz kolumny [10]\n🔹Wrzuć dane [11]"
                       f"\nWybierz opcję:  "))
    options = {
        1: load_csv,
        2: data_frames,
        3: pretty_info,
        4: delete_duplicates,
        5: delete_nulls,
        6: remove_column,
        7: rename_column,
        8: concat_dataframes,
        9: merge_dataframes,
        10: create_columns,
        11: load_frame
    }

    if selected_option in options:
        options[selected_option]()
    else:
        print("Źle wybrano")

    decision = None
    while decision != 'T' and decision != 'N':
        decision = input("Nie wybrano żadnej funkcji. Czy chcesz wybrać jeszcze raz? [N/T]: ").upper()
        if decision == 'T':
            fun_decision = True
        elif decision == 'N':
            fun_decision = False
            print("Do zobaczenia")
        else:
            print("Jeszcze raz")

