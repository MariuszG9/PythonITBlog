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

# wpisanie wartości typu null
df_animals.loc[2, 'Zwierze'] = None
df_animals.loc[3, 'Zwierze'] = np.nan
df_animals['Srodowisko'] = df_animals['Srodowisko'].replace(to_replace='LWP', value=None)
#df_animals['Srodowisko'] = df_animals['Srodowisko'].replace(['LWP', 'CSV'], [None, None])

# rekordy typu null
print(df_animals)
print(df_animals.isnull())
print("\n")
print(df_animals.isnull().sum())
print("\n")
print(df_animals.isnull().any())
print("\n")
print(df_animals.isnull().mean() * 100)
print("\n")
print(df_animals[df_animals['Srodowisko'].isnull()])
print("\n")
