from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msb

# Uruchamiam ramkę (okno)
window = Tk()

# Dodaję tytuł okna
window.title("Testujemy suwak!")


# Wielkość okna
x = window.winfo_screenwidth() // 3
y = int(window.winfo_screenheight() * 0.1)
window.geometry('400x400+' + str(x) + '+' + str(y))

# Tworzymy suwak
chg_val = StringVar()
zipper = Combobox(window, textvariable=chg_val)
zipper['values'] = ("Kiwi", "Banan", "Truskawka", "Jabłko", "Ananas")


# Ustawiamy wartość suwaka domyślną na kiwi
zipper.current(0)
zipper.place(x=150, y=50, anchor="center")


# Funkcja, która zwróci tekst
def on_changed(event):
    if chg_val == "Kiwi":
        msb.showinfo("Twój wybór", f"{chg_val.get()}, lubisz egzotyczne owoce")
    else:
        msb.showinfo("Twój wybór", f"{chg_val.get()}, lubisz polskie owoce")


# podpięcie metody pod zdarzenie podczas zmiany
zipper.bind("<<ComboboxSelected>>", on_changed)

window.mainloop()
