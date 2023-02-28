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

# możemy zrobić teraz te wszystkie operacje, które normalnie robilibyśmy na przykład z listą
rating_list = df_animals["Rating"].to_list()
print(len(rating_list))
print(round(sum(rating_list)/len(species_list), 2))
print("\n")

# możemy zrobić to normalnie seriami
rating_average = df_animals["Rating"].mean()
print(round(rating_average, 2))
print("\n")

# możemy też operować bezpośrednio na serii wpisanej w listę (można też na samej już serii, ale mniej czytelnie)
rating_avg = df_animals["Rating"]
print(f"Średnia: {round(rating_avg.mean(), 2)}, minimalna: {rating_avg.min()}, maksymalna: {rating_avg.max()}")
print("Średnia: {rating_avg:1.2f}".format(rating_avg=rating_avg.mean()))
print("\n")
