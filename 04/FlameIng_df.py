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
    try:
        df = pd.read_csv("Dane.csv", sep=";")
        df["affiliate_id"] = df['affiliate_id'].astype('object')
        df["affiliate_name"] = df['affiliate_name'].astype('str')
        df["group"] = df['group'].astype('str')
        df["commission"] = df["commission"].apply(lambda num: num.replace(',', '.')).astype(float)
        print(df)
    except:
        pass
        print("błąd")
    else:
        pass


print(f'Możliwe konfiguracje serwera: \n🔹0-testowy\n🔹1-produkcyjny')
server_number = int(input('Podaj cyfrę:'))
driver_xl, server_xl, database_xl = server_type(server_number)
print(f'Nazwa sterownika: {driver_xl}\nNazwa serwera: {server_xl}\nNazwa bazy: {database_xl}\n')

conn = connector()
cursor = conn.cursor()

load_dict_data()
