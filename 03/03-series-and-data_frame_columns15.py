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

# pamiętamy standardowe przywołanie kolumny (wielkość liter istotna, jeżeli kolumna z dużej to atrybut też)
# w pierwszym przypadku traktujemy bardziej jako słownik, w drugi jako obiekt
print(df_animals["Gatunek"])
print(df_animals.Gatunek)
print("\n")

# sortowanie danych po nowej kolumnie max
df_animals['max_rank'] = df_animals['Rating'].rank(method='max', ascending=False)
print(df_animals.max_rank)
print(df_animals.sort_values(by='max_rank'))
print("\n")

# Dodanie pustej kolumny
df_animals['Pusta kolumna'] = pd.NaT
print(f'Dodano pustą kolumnę do data frame df_animals \n {df_animals} \n')
# print(f"dane: {zwierzeta2['Pusta kolumna']}")

# Dodanie stałej wartości
df_animals['Stala_wartosciowa'] = 55
print(f'Dodano kolumnę ze stałą wartością 55 \n {df_animals} \n')

# Modyfikowanie zawartości kolumny
dzielna = 1000
new_animal_weight = [310/dzielna, 6.20/dzielna, 0.6/dzielna, 2/dzielna, 365/dzielna, 2.5/dzielna, 0.10/dzielna,
                     66/dzielna, 1/dzielna, 1/dzielna, 2/dzielna, 290/dzielna, 0.53/dzielna, 0.15/dzielna]
df_animals['Waga'] = new_animal_weight
print(f'Modyfikacja kolumny Waga w data frame o nazwie df_animals \n {df_animals} \n')

# Wypełnianie danych z jednej kolumny, danymi z innej
df_animals['Punkty EVS'] = df_animals['Rating']/2 + df_animals['Plywalnosc'].astype('int')/2
print(f'Nowa kolumna Punkty EVS w data frame o nazwie df_animals \n {round(df_animals, 2)} \n')

# Usuwanie niepotrzebnej kolumny
df_animals = df_animals.drop('Rating', axis=1)
print(f'Usunęliśmy Rating,\n {df_animals}')

# Sumowanie danych dla kolumn
print(df_animals.Waga.sum())

# Wartości Null
print(df_animals.isnull().sum())

# Odejmowanie danych w kolumnach
print(df_animals["Punkty EVS"] - df_animals.max_rank)

# Edytowanie wartości i maski na nową wartość
df_animals.loc[df_animals['Gatunek'] == 'Ptaki', 'Rating'] = 5
print(df_animals[df_animals['Gatunek'] == 'Ptaki'])

# Zmiana nazwy kolumny
df_animals = df_animals.rename(columns={'Rating':'Ocena', 'Pusta kolumna':'Pusta', 'Stala_wartosciowa':'Stala'})
print(df_animals)

# Szybkie łączenie kolumn
df_animals['Scalone'] = df_animals.Gatunek + '-' + df_animals.Srodowisko
print(df_animals)

# Szybkie łączenie kolumn
df_animals[['E1', 'E2']] = df_animals.Scalone.str.split('-', expand=True)
print(df_animals)

