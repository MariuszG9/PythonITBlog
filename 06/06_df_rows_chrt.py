import pandas as pd
import matplotlib.pyplot as plt

# utworzenie ramki danych
data = {
    'Zwierzę': ['Kucyk', 'Orzeł', 'Lemur', 'Pies', 'Świnia', 'Kangur', 'Bocian'],
    'Waga': [120, 15, 2, 20, 40, 60, 18],
    'Wzrost': [0.85, 1, 0.5, 0.6, 0.6, 2.2, 1.3],
    'Rodzaj': ['Ssaki', 'Ptaki', 'Ssaki', 'Ssaki', 'Ssaki', 'Ssaki', 'Ptaki'],
    'Liczba_nog': [4, 2, 4, 4, 4, 2, 2]
}
df_animals = pd.DataFrame(data)

# rysowanie wykresów

# wykres liniowy
plt.plot(df_animals['Zwierzę'], df_animals['Waga'], 'yo--')
for x, y in zip(df_animals['Zwierzę'], df_animals['Waga']):
    plt.text(x, y, str(y))
plt.title('Waga zwierząt')
plt.xlabel('Zwierzę')
plt.ylabel('Waga')
plt.show()


# wykres słupkowy
max_value = df_animals['Wzrost'].max()
colors = ['#FFD966' if value == max_value else '#0C5A4D' for value in df_animals['Wzrost']]
plt.barh(df_animals['Zwierzę'], df_animals['Wzrost'], color=colors)
plt.title('Wzrost zwierząt')
plt.xlabel('Zwierzę')
plt.ylabel('Wzrost')
plt.show()


# lista kolorów dla wykresu kołowego
colors = ['#2B3845', '#3B4D5F', '#4E667E', '#57738F', '#62809E', '#7E97B0', '#9DB0C3']

# rysowanie wykresu kołowego
plt.pie(df_animals['Waga'], labels=df_animals['Zwierzę'], colors=colors)
plt.title('Waga zwierząt')
plt.show()


# histogram
plt.hist(df_animals['Wzrost'], bins=3, edgecolor='black', color='#4E667E')
plt.title('Wzrost zwierząt')
plt.xlabel('Wzrost')
plt.ylabel('Liczba')
plt.show()


# ustawienia kolorów
line_color = '#777F7D'
bar_color = ['#168870' if w != max(df_animals['Wzrost']) else '#C2DF17' for w in df_animals['Wzrost']]

# rysowanie wykresów
fig, ax1 = plt.subplots()
fig.subplots_adjust(top=0.9, bottom=0.25, left=0.1, right=0.9)

# wykres liniowy
ax1.plot(df_animals['Zwierzę'], df_animals['Waga'], color=line_color, marker='o', label='Waga')
ax1.set_ylabel('Waga', color='gray')
ax1.tick_params(axis='y', labelcolor='gray')
for x,y in zip(df_animals['Zwierzę'], df_animals['Waga']):
    ax1.annotate(y, (x,y), textcoords="offset points", xytext=(0,10), ha='center', color=line_color)

# wykres słupkowy
ax2 = ax1.twinx()
ax2.bar(df_animals.index, df_animals['Wzrost'], color=bar_color, alpha=0.5, label='Wzrost')
ax2.set_ylabel('Wzrost', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
for x,y in zip(df_animals.index, df_animals['Wzrost']):
    ax2.annotate(y, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# dodanie legendy
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax2.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.24), ncol=2)

# dodanie tytułu i opisów osi
plt.title('Waga i wzrost zwierząt')
ax1.set_xlabel('Zwierzę')
ax1.set_xticks(df_animals.index)
ax1.set_xticklabels(df_animals['Zwierzę'], rotation=45, ha='right')
ax2.set_ylim(0, max(df_animals['Wzrost']) + 0.1)
plt.show()


# ustalenie koloru kółek na podstawie kolumny "Rodzaj"
colors = {'Ssaki': '#446BB2', 'Ptaki': '#3CBA69', 'Gady': 'green', 'Płazy': 'orange', 'Ryby': 'purple'}

# stworzenie scatter plotu
fig, ax = plt.subplots(figsize=(8, 6))
for _, row in df_animals.iterrows():
    ax.scatter(row['Waga'], row['Wzrost'], s=row['Liczba_nog']*100, c=colors[row['Rodzaj']], alpha=0.7, edgecolors='#C1C3C2')
    ax.annotate(row['Zwierzę'], (row['Waga'], row['Wzrost']), ha='center')

# dodanie tytułu i opisów osi
ax.set_title('Waga i wzrost zwierząt')
ax.set_xlabel('Waga')
ax.set_ylabel('Wzrost')

# dodanie legendy
for label, color in colors.items():
    ax.scatter([], [], c=color, alpha=0.7, s=50, edgecolors='black', label=label)
ax.legend(loc='upper left')
plt.show()

# obliczenie % udziału wagi w całości
weights = data['Waga']
total_weight = sum(weights)
percentages = [(weight/total_weight)*100 for weight in weights]

# kolory dla poszczególnych sektorów
colors = ['#0E6657', '#107665', '#13917C', '#1AC0A4', '#1DDDBD', '#59E9D1', '#A7F3E6']

# indeks wagi maksymalnej
max_weight_index = weights.index(max(weights))

# zmiana koloru dla wagi maksymalnej
colors[max_weight_index] = '#BA4A67'

# rysowanie wykresu pierścieniowego
fig, ax = plt.subplots(figsize=(11, 11))
wedges, labels, autopct = ax.pie(percentages, colors=colors, wedgeprops={'width': 0.5},
                                 autopct='%1.1f%%', startangle=90, pctdistance=0.85)

# zmiana koloru dla procentów wagi maksymalnej
wedges[max_weight_index].set_edgecolor('#BA4A67')

# ustawienia
plt.title('Udział wagi zwierząt')
plt.axis('equal')
plt.legend(wedges, data['Zwierzę'], title='Zwierzęta', bbox_to_anchor=(1.1, 0.5), loc='center left')
plt.subplots_adjust(left=0.1, right=0.75)

# wyświetlenie wykresu
plt.show()
