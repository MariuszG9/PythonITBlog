import pandas as pd

# utworzenie ramki danych
data = {'zwierze': ['Jaszczurka', 'Jastrząb', 'Okoń', 'Ptasznik', 'Rekin'],
        'waga': [0.1, 1.2, 2.5, 0.5, 500],
        'dlugosc_zycia': [3, 15, 10, 8, 70]}
df_animals = pd.DataFrame(data, index=['Jaszczurka', 'Jastrząb', 'Okoń', 'Ptasznik', 'Rekin'])

# wybieramy wiersz po etykiecie
ptasznik = df_animals.loc['Ptasznik']
print(ptasznik)

# filtrowanie po etykiecie i kolumnie 'waga'
ptasznik_waga = df_animals.loc['Ptasznik', 'waga']
print(ptasznik_waga)

# filtrowanie za pomocą warunku logicznego (AND)
ptasznik_rekin = df_animals.loc[(df_animals.index == 'Ptasznik') | (df_animals.index == 'Rekin')]
print(ptasznik_rekin)
