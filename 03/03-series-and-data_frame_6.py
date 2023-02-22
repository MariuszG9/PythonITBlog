import pandas as pd

# tworzymy dwie krótkie ramki danych
lewa = pd.DataFrame({'klucz': ['1', '2', '3', '4'],
                    'X': ['Biały', 'Czarny', 'Niebieski', 'Zielony']})

prawa = pd.DataFrame({'klucz': ['0', '1', '2', '3'],
                    'Y': ['Red', 'White', 'Black', 'Blue']})

# ramki danych
print(lewa)
print("\n")
print(prawa)

# merge możemy połączyć na kluczach
df_keymerge = pd.merge(lewa, prawa, right_index=True, left_index=True, suffixes=('_01', '_02'))
print(df_keymerge)
print("\n")

# merge w którym najpierw resetujemy indexy, a potem łączymy na kolumnach
df_resetindex = pd.merge(lewa.reset_index(), prawa.reset_index(), on=['klucz'])
print(df_resetindex)
print("\n")

# merge outer (zewnętrzne)
df_outer_indi = pd.merge(lewa, prawa, how='outer', indicator=True)
print(df_outer_indi)
print("\n")

# merge złączenie do czegoś
df_mergeto = lewa.merge(prawa, left_on='klucz', right_on='klucz', how='left')
print(df_mergeto)
print("\n")

# merge z walidacją
df_mege_valid = lewa.merge(prawa, left_on='klucz', right_on='klucz', how='inner', validate="one_to_one")
print(df_mege_valid)
