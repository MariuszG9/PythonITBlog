import pandas as pd

# tworzymy dwie krótkie ramki danych
lewa = pd.DataFrame({'klucz': ['1', '2', '3', '4'],
                    'X': ['Biały', 'Czarny', 'Niebieski', 'Zielony']})

prawa = pd.DataFrame({'klucz': ['0', '1', '2', '3'],
                    'Y': ['Red', 'White', 'Black', 'Blue']})

# ramki danych
#print(lewa)
#print("\n")
#print(prawa)

# join po index z sufiksami
join_on_index = lewa.join(prawa, lsuffix='_lewa', rsuffix='_prawa')
print(join_on_index)
print("\n")

# join po kluczu - błędnie
join_on_key_wrong = lewa.join(prawa, on='klucz')
print(join_on_key_wrong)
print("\n")

# join po kluczu - poprawnie
join_on_key = lewa.join(prawa.set_index('klucz'), on='klucz')
print(join_on_key)
print("\n")

# join left
join_left = lewa.join(prawa.set_index('klucz'), on='klucz', how='left', sort=True)
print(join_left)
print("\n")

# join right
join_right = lewa.join(prawa.set_index('klucz'), on='klucz', how='right', validate='1:1')
print(join_right)
print("\n")

# join outer
join_outer = lewa.join(prawa.set_index('klucz'), on='klucz', how='outer')
print(join_outer)
print("\n")

# join inner
join_inner = lewa.join(prawa.set_index('klucz'), on='klucz', how='inner')
print(join_inner)
print("\n")
