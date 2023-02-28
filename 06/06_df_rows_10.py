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


# rozmiar ramki danych w postaci krotki
print(df_animals.shape)
num_rows = df_animals.shape[0]  # liczba wierszy
num_cols = df_animals.shape[1]  # liczba kolumn
print(f'Mamy dokładnie {num_rows} wierszy oraz {num_cols} kolumn')
print("\n")
