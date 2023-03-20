import pandas as pd
import os
from prettytable import PrettyTable
import json
import pyodbc
import logging
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


fun_decision = True
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)


def load_csv():
    path = os.path.dirname(__file__)
    extension = ".csv"
    df_list = []
    df_dict = {}
    files = [file[:-len(extension)] for file in os.listdir(path) if file.endswith(extension)]
    for file in files:
        csv_file = os.path.join(path, file + extension)
        if os.path.isfile(csv_file):
            decimal = ',' if pd.read_csv(csv_file, sep=';', encoding='utf-8', nrows=1).iloc[0].str.contains(',').any() else '.'
            df_name = "df_" + file.lower()
            df_dict[df_name] = pd.read_csv(csv_file, sep=";", encoding='utf-8', decimal=decimal)
            print(f"Utworzono ramkę danych {df_name} z pliku {file}.csv")
            df_list.append(file)
    data_frame_operation(f"wczytano ramkę danych {df_list}")
    return df_dict


def data_frames(df_dict):
    df_list = []
    print("Utworzone ramki danych:")
    for var in df_dict:
        if isinstance(df_dict[var], pd.DataFrame):
            print(var)
            print(f'{df_dict[var]}\n')
            df_list.append(var)
    data_frame_operation(f"Wypisano ramki {df_list}")


def pretty_info(df_dict):
    df_list = []
    for df_name, df in df_dict.items():
        table = PrettyTable()
        null_count = df.isnull().sum().sum()
        nan_count = df.isna().sum().sum()
        table.field_names = [''] + list(df.describe(include='all').columns)
        for i, row in enumerate(df.describe(include='all').itertuples()):
            table.add_row([f"{row[0]}"] + [f"{x:.2f}" if isinstance(x, (int, float)) else x for x in row[1:]])
        print(f"Statystyki dla ramki danych {df_name}:")
        print(table)
        print(f"Liczba duplikatów: {df.duplicated().sum()}")
        print(f"Liczba wartości: NULL = {null_count} | NaN: {nan_count}\n")
        df_list.append(df_name)
    data_frame_operation(f"Wypisano statystyki dla ramki danych {df_list}")


def delete_duplicates(df_dict):
    duplicates_removed = {}
    for df_name, df in df_dict.items():
        n_before = len(df)
        df.drop_duplicates(inplace=True)
        n_after = len(df)
        if n_before != n_after:
            duplicates_removed[df_name] = n_before - n_after
            print(f"Usunięto {duplicates_removed[df_name]} duplikatów z ramki danych {df_name}")
            pretty_info({df_name: df})
    data_frame_operation(f"Usunięto duplikaty z ramek danych: {duplicates_removed}")


def delete_nulls(df_dict):
    no_nulls = []
    nulls_removed = 0
    null_invoices = {}
    for df_name, df in df_dict.items():
        null_count = df.isnull().sum().sum()
        if null_count == 0:
            no_nulls.append(df_name)
        else:
            null_invoices[df_name] = df.loc[df.isnull().any(axis=1), 'invoice_num'].tolist()
            df_dict[df_name] = df.dropna()
            nulls_removed += null_count
            print(f"Usunięto {null_count} wartości NULL z ramki danych {df_name}. Numery faktur: {', '.join(str(inv) for inv in null_invoices[df_name])}")
            data_frame_operation(f"Usunięto {null_count} wartości NULL z ramki danych {df_name}. Numery faktur: {', '.join(str(inv) for inv in null_invoices[df_name])}")
    if null_invoices:
        for df_name in no_nulls:
            print(f"Nie znaleziono wartości NULL w ramce danych {df_name}")
    else:
        nulls_removed += 1


def remove_column(df_dict):
    # Wypisz dostępne ramki danych
    data_frames_list = list(df_dict.keys())
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
            df = df_dict[df_name]
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
    data_frame_operation(f"Usunięto kolumnę '{col_name}' z ramki danych '{df_name}'.")


def rename_column(df_dict):
    # Wydruk dostępnych ramek
    print("Dostępne ramki danych:")
    dataframes = list(df_dict.keys())
    table = PrettyTable()
    table.field_names = ["Numer", "Nazwa"]
    for i, df in enumerate(dataframes, 1):
        table.add_row([i, df])
    print(table)

    while True:
        try:
            df_choice = int(input("Wybierz numer ramki danych: ")) - 1
            df_name = dataframes[df_choice]
            df = df_dict[df_name]
            columns = df.columns.tolist()
            table = PrettyTable()
            table.field_names = ["Numer", "Nazwa kolumny"]
            for i, col in enumerate(columns, 1):
                table.add_row([i, col])
            print(table)
            col_choice = int(input("Wybierz numer kolumny, którą chcesz zmienić nazwę: ")) - 1
            old_col_name = columns[col_choice]
            break
        except ValueError:
            print("Podano nieprawidłową wartość. Wybierz liczbę z przedziału [1, {}]".format(len(dataframes)))
        except IndexError:
            print("Podano nieprawidłowy numer ramki danych. Wybierz liczbę z przedziału [1, {}]".format(len(dataframes)))
        except:
            print("Wystąpił nieznany błąd. Spróbuj ponownie.")

    # Zapytamy o nazwę nowej kolumny
    new_col_name = input("Podaj nową nazwę dla kolumny: ")

    # zmieniamy nazwę kolumny
    df.rename(columns={old_col_name: new_col_name}, inplace=True)

    # Drukujemy nagłówek z ramki
    print(f"\nKolumna {old_col_name} w ramce danych {df_name} zmieniła nazwę na {new_col_name}.\n")
    print(df.head())

    # Aktualizujemy słownik df_dict
    df_dict[df_name] = df
    data_frame_operation(f"Kolumna {old_col_name} w ramce danych {df_name} zmieniła nazwę na {new_col_name}")
    return df_dict


def concat_dataframes(df_dict):
    mask = 'df_sales_'
    dfs = [v for k, v in df_dict.items() if k.startswith(mask)]
    merged_df = pd.concat(dfs)
    df_list = [k for k, v in df_dict.items() if k.startswith(mask)]
    if len(dfs) > 1:
        data_frame_operation(f"Połączono ramki danych: {df_list}")
    else:
        data_frame_operation(f"Nie ma co łączyć - w słowniku jest tylko jedna ramka danych pasująca do wzorca {mask}")
    df_dict['merged_df'] = merged_df
    print(merged_df.head())
    return merged_df


def merge_dataframes(df_dict):
    df_salesman = df_dict['df_salesman']
    merged_df = df_dict['merged_df']
    merged_df_with_salesman = pd.merge(merged_df, df_salesman[['salesman_id', 'surname']], on='salesman_id', how='left')
    df_dict['merged_df_with_salesman'] = merged_df_with_salesman
    data_frame_operation(f"Połączono ramki danych: df_salesman oraz merged_df")
    print(merged_df_with_salesman.head())
    return merged_df_with_salesman


def create_columns(df_dict):
    df = df_dict['merged_df_with_salesman']
    df['value_up'] = df['value'] * 1.08

    # Obliczenie kolumny "rebate_value"
    df['rebate_value'] = df['value']
    df.loc[df['quantity'] > 10000, 'rebate_value'] *= 0.9

    # Obliczenie kolumny "price_per_unit"
    df['price_per_unit'] = 0
    mask = df['quantity'] != 0
    df.loc[mask, 'price_per_unit'] = df.loc[mask, 'value'] / df.loc[mask, 'quantity']
    df_dict['merged_df_database'] = df
    print(df)
    data_frame_operation(f"Połączono ramki danych: df_salesman oraz merged_df")
    df.to_csv('ramka_wynikowa.csv', sep=';', index=False)


def load_frame(df_dict):
    table_data = []
    table_name = 'sales_per_country'
    server_connect = None
    df = df_dict['merged_df_database']
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


def data_analyze():
    # wczytaj dane z pliku csv
    merged_df_database = pd.read_csv('ramka_wynikowa_eur.csv', sep=";", encoding='utf-8')

    # kolory linii i markerów
    line_colors = ['#8497B0', '#F6DD60', '#06A297']
    marker_colors = ['#5E7594', '#F2CD16', '#047068']

    # stwórz wykres słupkowy
    fig, ax = plt.subplots()
    ax.bar(merged_df_database.index, merged_df_database['quantity'], color='gray', alpha=0.6, edgecolor='none',
           width=0.8, label='quantity', capstyle='round')

    # stwórz trzy linie wykresu
    for i, col in enumerate(['value', 'value_up', 'rebate_value']):
        ax.plot(merged_df_database.index, merged_df_database[col], lw=4, solid_capstyle='round',
                color=line_colors[i], marker='o', markerfacecolor=marker_colors[i], markeredgecolor=marker_colors[i],
                linestyle='-', label=col)

        # dodaj etykietę 'max' nad wartością największą na linii 'value_up'
        for x, y, v in zip(merged_df_database.index, merged_df_database[col], merged_df_database[col]):
            if col == 'value_up' and v == max(merged_df_database['value_up']):
                ax.text(x, y + (max(merged_df_database['value_up']) * 0.01), 'max', ha='center', va='bottom',
                        fontsize=10)
            else:
                ax.text(x, y, '', ha='center', va='top', fontsize=10)

    # wyświetl legendę oraz dodaj tytuł i etykiety osi
    ax.legend()
    ax.set_title('Wykres danych')
    ax.set_xlabel('Kategorie')  # zmieniono etykietę osi x na 'Kategorie'
    ax.set_ylabel('Ilość')

    # zmiana formatowania osi y - wyświetlanie wartości w tysiącach
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0f}k'.format(y / 1000)))

    # dodaj wartości słupków nad słupkami
    for x, y, q in zip(merged_df_database.index, merged_df_database['quantity'], merged_df_database['quantity']):
        ax.text(x, y - (max(merged_df_database['quantity']) * 0.05), '{:.0f}k'.format(q / 1000), ha='center', va='top',
                fontsize=10)

    # dodaj siatkę pionową oraz ukryj etykiety osi x
    if 'value' in merged_df_database.columns:
        ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.6)
        ax.tick_params(labelbottom=True)  # zmieniono wartość labelbottom na True, aby wyświetlać etykiety osi x

    # wyświetl wykres
    plt.show()


logger = setup_logging('plik_logow.txt')

while fun_decision:
    selected_option = int(input(f"Którą funkcję chcesz wywołać?\n🔹Załadowanie ramek danych [1]"
                       f"\n🔹Wypisanie ramek danych [2]\n🔹Informacje o ramkach [3]\n🔹Usuń duplikaty [4]"
                       f"\n🔹Usuń rekordy z NULL'ami [5]\n🔹Usuń kolumny [6]\n🔹Zmień nazwę kolumny [7]"
                       f"\n🔹Połącz ramki o masce df_salesman_* [8]\n🔹Dołącz tabelę Salesman [9]"
                       f"\n🔹Utwórz kolumny [10]\n🔹Wrzuć dane [11]\n🔹Analizuj dane wykres1 [12]"
                       f"\nWybierz opcję:  "))
    if selected_option == 1:
        df_dict = load_csv()
    elif selected_option == 2:
        data_frames(df_dict)
    elif selected_option == 3:
        pretty_info(df_dict)
    elif selected_option == 4:
        delete_duplicates(df_dict)
    elif selected_option == 5:
        delete_nulls(df_dict)
    elif selected_option == 6:
        remove_column(df_dict)
    elif selected_option == 7:
        rename_column(df_dict)
    elif selected_option == 8:
        concat_dataframes(df_dict)
    elif selected_option == 9:
        merge_dataframes(df_dict)
    elif selected_option == 10:
        create_columns(df_dict)
    elif selected_option == 11:
        load_frame(df_dict)
    elif selected_option == 12:
        data_analyze()
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


