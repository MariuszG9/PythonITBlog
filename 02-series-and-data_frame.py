# zaimportowanie biblioteki
import pandas as pd

# seria danych zawierająca kilka liczb całkowitych, przykładowo kategorię mglistości (1-niska, 7-wysoka)
series_fog_level = pd.Series([1, 2, 4, 4, 7, 2, 1])

# ramka danych, wczytanie danych z pliku płaskiego CSV
data_frame = pd.read_csv("weather_data.csv")

# print danych z serii i z ramki danych
print(series_fog_level)
print(data_frame["temperature"])
