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
server_switch= int(input('Podaj cyfrę:'))
driver, server, database = server_type(server_switch)
print(f'Nazwa sterownika: {driver}\nNazwa serwera: {server}\nNazwa bazy: {database}')
