import pandas as pd

# tworzymy dwie krótkie ramki danych
lewa = pd.DataFrame({'klucz': ['1', '2', '3', '4'],
                       'X': ['X1', 'X2', 'X3', 'X4']})

prawa = pd.DataFrame({'klucz': ['0', '1', '2', '3'],
                       'Y': ['Y0', 'Y1', 'Y2', 'Y3']})

# merge po kolumnie
df_metoda = pd.merge(lewa, prawa, on='klucz')
print(df_metoda)
print("\n")

# merge outer (zewnętrzne)
df_outer = pd.merge(lewa, prawa, how='outer')
print(df_outer)
print("\n")

# merge inner (wewnętrzny)
df_inner = pd.merge(lewa, prawa, how='inner')
print(df_inner)
print("\n")

# merge left (do lewych dołączam, prawe które występują)
df_left = pd.merge(lewa, prawa, how='left')
print(df_left)
print("\n")

# merge right (do prawych dołączam, lewe które występują)
df_right = pd.merge(lewa, prawa, how='right')
print(df_right)
