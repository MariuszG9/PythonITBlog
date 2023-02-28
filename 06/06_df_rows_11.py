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

# informacje o ramce
print(df_animals.info())
print("\n")
# wyświetlenie dodatkowych informacji i liczbę brakujących wartości
df_animals.info(verbose=True, null_counts=True)
print("\n")
# dokładne obliczenie zużycia pamięci
df_animals.info(memory_usage='deep')
print("\n")
