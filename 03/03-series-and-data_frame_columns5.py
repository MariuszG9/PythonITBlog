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

# Modyfikowanie zawartości kolumny
dzielna = 1000
new_animal_weight = [310/dzielna, 6.20/dzielna, 0.6/dzielna, 2/dzielna, 365/dzielna, 2.5/dzielna, 0.10/dzielna,
                     66/dzielna, 1/dzielna, 1/dzielna, 2/dzielna, 290/dzielna, 0.53/dzielna, 0.15/dzielna]
df_animals['Waga'] = new_animal_weight
print(f'Modyfikacja kolumny Waga w data frame o nazwie df_animals \n {df_animals} \n')
