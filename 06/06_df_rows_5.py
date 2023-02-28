# zaimportowanie biblioteki
import pandas as pd

# wyświetlenie większej ilości kolumn
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)

# wczytanie danych / należy zwrócić uwagę na sep i decimal xxx
df_first = pd.read_csv("Dane_01.csv", sep=";", decimal=',')
df_second = pd.read_csv("Dane_02.csv", sep=";")

# łączenie danych metodą merge xxx
df_animals = pd.merge(df_first, df_second, how='outer')

# pobranie danych z wiersza
print(df_animals[df_animals.Gatunek == "Ssaki"])
print("\n")
df_slice = df_animals[(df_animals['Gatunek'] == "Ssaki") | (df_animals['Gatunek'] == "Ptaki")]
print(df_slice)
print("\n")
print(df_animals[df_animals.Waga == df_animals.Waga.max()])
print("\n")
