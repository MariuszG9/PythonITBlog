import pyodbc

# Utworzenie połączenia do bazy danych
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=my_server;DATABASE=my_database;UID=my_username;PWD=my_password')

# Utworzenie obiektu cursor
cursor = conn.cursor()

# Wykonanie zapytania SQL
cursor.execute("SELECT * FROM super_table")

# Pobranie wyników zapytania
rows = cursor.fetchall()

# Wyświetlenie wyników
for row in rows:
    print(row)
