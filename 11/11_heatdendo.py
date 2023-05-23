# Import istotnych bibliotek
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Załadowanie danych
country_data = pd.read_csv('Country clusters.csv', index_col='Country')

cc_scaled = country_data.copy()
cc_scaled = cc_scaled.drop(['Language'], axis=1)

# Kreślenie danych
sns.clustermap(cc_scaled, cmap='mako')
plt.show()
