import pandas as pd
import numpy as np

# tworzenie DataFrame z wartościami NaN i NaT
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, 7, 8, np.nan, pd.NaT],
    'C': [pd.Timestamp('2023-02-20'), pd.Timestamp('2023-02-21'), pd.NaT, pd.Timestamp('2023-02-23'), pd.Timestamp('2023-02-24')]
})

# wyświetlenie DataFrame
print(df)
print(f'\n')

# uzupełnienie wartości NaN w kolumnie A średnią wartością z tej kolumny
df['A'] = df['A'].fillna(df['A'].mean())

# wyświetlenie DataFrame po uzupełnieniu wartości NaN
print(df)
print(f'\n')

# wyświetlenie wierszy zawierających wartość NaT w kolumnie C
print(df[df['C'].isna()])
print(f'\n')

# konwersja wartości NaT w kolumnie C na datę '2022-02-22'
df.loc[df['C'].isna(), 'C'] = pd.to_datetime('2022-02-22')

# wyświetlenie DataFrame po konwersji wartości NaT w kolumnie C
print(df)
print(f'\n')

# zapisanie DataFrame do pliku CSV
df.to_csv('data.csv', index=False)
