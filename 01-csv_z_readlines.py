# zapisujemy nazwę pliku do stałej
OPEN_FILE = "weather_data.csv"

# otwieramy plik z with-open
with open(OPEN_FILE) as data_file:
    weather_data = data_file.readlines()


# w tym momencie w pętli zagnieżdżamy instrukcję warunkową
#   jeżeli dotyczy to pierwsze wiersza [index = 0] to traktujemy go jako nagłówek
#   jeżeli warunek nie jest spełniony to są to wiersze z danymi
# wykorzystałem "f-string" ponieważ znacznie upraszcza zapis i dla mnie czyni go przejrzystym.
# end pozwala mi w tym konktekście pozbyć znaku końca linii \n
def print_table_elements():
    for row in range(0, 8):
        if row == 0:
            print(f'Nagłówek: {weather_data[row]}', end='')
        else:
            print(f'Wiersz {row} : {weather_data[row]}', end='')


# wywołuje moją funkcję
print_table_elements()
