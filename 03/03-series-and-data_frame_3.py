# zaimportowanie biblioteki
import pandas as pd

# wyświetlenie większej ilości kolumn
desired_width = 350
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 15)

# wczytanie danych / należy zwrócić uwagę na sep i decimal
df_first = pd.read_csv("Dane_01.csv", sep=";", decimal=',')
df_second = pd.read_csv("Dane_02.csv", sep=";")

# łączenie danych metodą concat()
df_animals = pd.concat([df_first, df_second], axis=0, ignore_index=True)

# sortujemy dane
df_animals = df_animals.sort_values(by=['Gatunek'], ascending=True)

print(df_animals)

