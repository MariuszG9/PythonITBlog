# zaimportowanie biblioteki
import pandas as pd

# tworzymy słownik list
slownik_zwierzat = {'Gatunek': ['Ssaki',
                                'Ptaki',
                                'Płazy',
                                'Gady',
                                'Ryby'
                              ],
                  'Zwierze': ['Tygrys',
                              'Tukan',
                              'Żaba',
                              'Jaszczurka',
                              'Rekin'
                             ]
                 }

# tworzymy ramkę danych
zwierzeta = pd.DataFrame(slownik_zwierzat)

# zamiana indeksów na własne
zwierzeta.index = ['SS', 'PT', 'PL', 'GA', 'RY']

print(zwierzeta)
