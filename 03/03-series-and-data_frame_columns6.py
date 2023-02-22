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

# Wypełnianie danych z jednej kolumny, danymi z innej
df_animals['Punkty EVS'] = df_animals['Rating']/2 + df_animals['Plywalnosc'].astype('int')/2
print(f'Nowa kolumna Punkty EVS w data frame o nazwie df_animals \n {round(df_animals, 2)} \n')
