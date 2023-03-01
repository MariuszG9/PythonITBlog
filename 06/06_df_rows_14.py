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
df_duplicate = pd.read_csv("Dane_03_dup.csv", sep=";", decimal=',')

# łączenie danych metodą merge xxx
df_animals = pd.merge(df_first, df_second, how='outer')

# wpisanie wartości typu null
df_animals.loc[2, 'Zwierze'] = 'Tygrys'

# duplikaty
print(df_animals.duplicated())
print('\n')
print(df_animals['Zwierze'].duplicated().sum())
print('\n')
print(df_animals.duplicated().sum())
print('\n')
df_animals['Zwierze_duplicated'] = df_animals['Zwierze'].duplicated(keep=False)
print(df_animals['Zwierze_duplicated'])
print('\n')
print(df_duplicate.duplicated())
print('\n')
print(df_duplicate)
print('\n')
print(df_duplicate.drop_duplicates())

duplicates_total = df_duplicate.duplicated().sum()
print(f'Usunięto {duplicates_total}')
