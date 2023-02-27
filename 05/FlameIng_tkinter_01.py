from tkinter import *

# Uruchamiam ramkę (okno)
window = Tk()

# Wielkość okna
x = window.winfo_screenwidth() // 3
y = int(window.winfo_screenheight() * 0.1)
window.geometry('300x400+' + str(x) + '+' + str(y))

# Dodaję tytuł okna
window.title("Sałatka owocowa")
window.configure(bg="#1F4C55")

# Tworzę napis w oknie
which_fruit = Label(window, text="Jaki lubisz owoc?", bg="#1F4C55", fg="white")

# Ustawiam gdzie ten napis ma być ulokowany
which_fruit.grid(column=0, row=0)

# Wcięcie do wpisania owocu oraz zdefiniowane pozycji, tutaj pozycja za pomocą .grid()
fruit = Entry(window, width=20, bg="#FFD966", fg="#1B4149")
fruit.grid(column=1, row=0)


def clicked():
    # Ustawiamy kolejny label odpowiedzialny za całość tekstu
    which_fruit2 = Label(window, bg="#1F4C55", fg="white")
    # Przypisujemy tekst + wartość ze zmiennej
    fruit2 = "Sałatka na podstawie  " + fruit.get()
    # Wypisujemy dane do labela
    which_fruit2.configure(text=fruit2, font=("TkMenuFont", 10))
    # Ustalamy pozycję na podstawie place
    which_fruit2.place(x=150, y=50, anchor="center")


main_button = Button(window, text="Wymiksuj sałatkę", command=clicked)

# Położenie przycisku w dwóch wariantach
# main_button.grid(column=1, row=3)
main_button.place(x=95, y=130)

# Uruchomienie pętli aplikacji
window.mainloop()
