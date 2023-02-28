import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]})

# pobranie wartości z ramki danych i konwersja na listę
data_list = df.values.tolist()

# wyświetlenie listy
print(data_list)
