import pandas as pd

# przykładowe dane
df = pd.DataFrame({'name': ['Anna', 'Jan', 'Adam', 'Daria'],
                   'age': [28, 29, 18, 45],
                   'gender': ['F', 'M', 'M', 'F']})

# filtrowanie po wartości kolumny 'age'
df_filtered = df[df['age'] > 28]
print(df_filtered)
print('\n')

# filtrowanie po wartościach w dwóch kolumnach
df_filtered = df[(df['age'] > 20) & (df['gender'] == 'M')]
print(df_filtered)
print('\n')

# filtrowanie po wartościach w jednej kolumnie i pochodzących z listy
names = ['Anna', 'Daria']
df_filtered = df[df['name'].isin(names)]
print(df_filtered)
print('\n')
