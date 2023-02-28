# zaimportowanie biblioteki
import pandas as pd
from prettytable import PrettyTable
import numpy as np

# wyświetlenie większej ilości kolumn
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)

# wczytanie danych / należy zwrócić uwagę na sep i decimal xxx
df_first = pd.read_csv("Dane_01.csv", sep=";", decimal=',')
df_second = pd.read_csv("Dane_02.csv", sep=";")

# łączenie danych metodą merge xxx
df_animals = pd.merge(df_first, df_second, how='outer')

# unikalne rekordy
print(df_animals.describe())
print("\n")
print(df_animals.describe(include='all'))
print("\n")

# wyświetlenie wyników opisowych za pomocą PrettyTable
table = PrettyTable()
table.field_names = [''] + list(df_animals.describe().columns)
for i, row in enumerate(df_animals.describe().itertuples()):
    if i == 0:
        table.add_row(['count'] + list(np.round(row[1:], 2)))
    elif i == 1:
        table.add_row(['mean'] + list(np.round(row[1:], 2)))
    elif i == 2:
        table.add_row(['std'] + list(np.round(row[1:], 2)))
    elif i == 3:
        table.add_row(['min'] + list(np.round(row[1:], 2)))
    elif i == 4:
        table.add_row(['25%'] + list(np.round(row[1:], 2)))
    elif i == 5:
        table.add_row(['50%'] + list(np.round(row[1:], 2)))
    elif i == 6:
        table.add_row(['75%'] + list(np.round(row[1:], 2)))
    elif i == 7:
        table.add_row(['max'] + list(np.round(row[1:], 2)))
print(table)
