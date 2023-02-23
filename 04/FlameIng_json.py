import json

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


print(f'Możliwe konfiguracje serwera: \n🔹0-testowy\n🔹1-produkcyjny')
server_number = int(input('Podaj cyfrę:'))
driver_xl, server_xl, database_xl = server_type(server_number)
print(f'Nazwa sterownika: {driver_xl}\nNazwa serwera: {server_xl}\nNazwa bazy: {database_xl}')
