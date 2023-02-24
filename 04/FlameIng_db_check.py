import json
import pyodbc
import pandas as pd

with open('server_config.json') as sc:
    data = json.load(sc)


def server_type(server_switch):
    server_connect = None
    server = data['servers']
    if server_switch == 0:
        server_connect = server[0]
    elif server_switch == 1:
        server_connect = server[1]
    else:
        print("zły profil")

    driver = server_connect['DRIVER']
    server = server_connect['SERVER']
    database = server_connect['DATABASE']

    return driver, server, database


def connector():
    connectorx = pyodbc.connect('driver=' + driver_xl + ';'
                          'server=' + server_xl + ';'
                          'database=' + database_xl + ';'
                          'Trusted_Connection=yes')
    return connectorx


def load_dict_data():
    table_name = 'affiliate_dict'
    try:
        df = pd.read_csv("Dane.csv", sep=";", encoding='utf-8')
        df["affiliate_id"] = df['affiliate_id'].astype('object')
        df["affiliate_name"] = df['affiliate_name'].astype('str')
        df["group"] = df['group'].astype('str')
        df["commission"] = df["commission"].apply(lambda num: num.replace(',', '.')).astype(float)

        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()
        for index, row in df.iterrows():
            row = list(row)
            query_sql = f"""INSERT INTO {table_name} (affiliate_id, affiliate_name, commission, group_name) 
                        VALUES (?,?,?,?)"""
            cursor.execute(query_sql, row)
            conn.commit()

        print(f'Dane z tabeli {table_name} zostały usunięte oraz dodano nowe.')
        cursor.execute(f'SELECT * FROM {table_name} ORDER BY affiliate_name')
        table_rows = cursor.fetchall()
        for row in table_rows:
            print(row)
 
    except:
        pass
        print("błąd")


print(f'Możliwe konfiguracje serwera: \n🔹0-testowy\n🔹1-produkcyjny')
server_number = int(input('Podaj cyfrę:'))
driver_xl, server_xl, database_xl = server_type(server_number)
print(f'Nazwa sterownika: {driver_xl}\nNazwa serwera: {server_xl}\nNazwa bazy: {database_xl}\n')

conn = connector()
cursor = conn.cursor()

load_dict_data()
