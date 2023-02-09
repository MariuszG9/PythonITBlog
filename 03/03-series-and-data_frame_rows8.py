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

# wrzucenie ramki danych do słownika
animals_dict = df_animals.to_dict()
print(animals_dict)
print("\n")

# wrzucenie serii do listy
species_list = df_animals["Gatunek"].to_list()
print(species_list)
print("\n")

# możemy zrobić teraz te wszystkie operacje, które normalnie robilibyśmy na przykład z listą
rating_list = df_animals["Rating"].to_list()
print(len(species_list))
print(round(sum(rating_list)/len(species_list), 2))
print("\n")

# możemu zrobić to normalnie seriami
rating_average = df_animals["Rating"].mean()
print(round(rating_average, 2))
print("\n")

# możemy też operować bezpośrednio na seri wpisanej w listę (można też na samej już serii, ale mniej czytelnie)
rating_avg = df_animals["Rating"]
print(f"Średnia: {round(rating_avg.mean(), 2)}, minimalna: {rating_avg.min()}, maksymalna: {rating_avg.max()}")
print("Średnia: {rating_avg:1.3f}.format(rating=result")
print("\n")

# pamiętamy standardowe przywołanie kolumny (wielkość liter istotna, jeżei kolumna z dużej to atrybut też)
# w pierwszym przypadku traktujemy bardziej jako słownik, w drugi jako obiekt
print(df_animals["Gatunek"])
print(df_animals.Gatunek)
print("\n")

# sortowanie dnaych po nowej kolumnie max
df_animals['max_rank'] = df_animals['Rating'].rank(method='max', ascending=False)
print(df_animals.max_rank)
print(df_animals.sort_values(by='max_rank'))
print("\n")

# Dodanie pustej kolumny
df_animals['Pusta kolumna'] = pd.NaT
print(f'Dodano pustą kolumnę do data frame zwierzeta2 \n {df_animals} \n')
# print(f"dane: {zwierzeta2['Pusta kolumna']}")

# Dodanie stałej wartości
df_animals['Stala_wartosciowa'] = 55
print(f'Dodano kolumnę ze stałą wartością 55 \n {df_animals} \n')

# Modyfikowanie zawartości kolumny
dzielna = 1000
new_animal_weight = [310/dzielna, 6.20/dzielna, 0.6/dzielna, 2/dzielna, 365/dzielna, 2.5/dzielna, 0.10/dzielna,
                     66/dzielna, 1/dzielna, 1/dzielna, 2/dzielna, 290/dzielna, 0.53/dzielna, 0.15/dzielna]
df_animals['Waga'] = new_animal_weight

print(f'Modyfikacja kolumny Waga w data frame o nazwie zwierzęta2 \n {df_animals} \n')

# Wypełnianie danych z jednej kolumny, danymi z innej
df_animals['Punkty EVS'] = df_animals['Rating']/2 + df_animals['Plywalnosc'].astype('int')/2
print(f'Nowa kolumna Punkty EVS w data frame o nazwie zwierzęta2 \n {round(df_animals, 2)} \n')

# Usuwanie niepotrzebnej kolumny
df_animals = df_animals.drop('Rating', axis=1)
print(f'Nowa kolumna Punkty EVS w data frame o nazwie zwierzęta2 \n {round(df_animals, 2)} \n')

# Pobranie wybranej kolumny
print(df_animals["Zwierze"])
print(df_animals.Zwierze)
