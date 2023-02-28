import pandas as pd

# utworzenie ramki danych
df = pd.DataFrame({
    'Waga': [5, 2, 10],
    'Dlugosc_zycia': [2, 5, 7]
}, index=['Jaszczurka', 'Jastrzab', 'Okon'])

# wyświetlenie wartości dla Jastrzębia za pomocą metody .loc()
print(df.loc['Jastrzab'])
