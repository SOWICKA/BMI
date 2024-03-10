# KODOWAL : Kamil Sulewski
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

def oblicz_bmi(waga, wzrost):
    waga2 = waga.replace(",", ".")
    wzrost2 = wzrost.replace(",", ".")

    try:
        waga_float = float(waga2)
        wzrost_float = float(wzrost2)

        if waga_float > 0 and wzrost_float > 0:
            bmi_wynik = waga_float / ((wzrost_float * 0.01) ** 2)
            return round(bmi_wynik, 2)
        else:
            raise ValueError("Wartości wagi i wzrostu muszą być dodatnie.")
    except ValueError as e:
        raise e

def interpretuj_bmi(bmi):
    if 16 > bmi > 0:
        return "OJEJ Twoje BMI świadczy o skrajnym wychudzeniu :(" \
               "\nZalecamy szybki kontakt z pomocą medyczną!"
    elif 16 <= bmi <= 16.99:
        return "Ups... Twoje BMI wskazuje na wychudzenie :(" \
               "\nZachęcamy do poszukania pomocy"
    elif 17 <= bmi <= 18.49:
        return "NIEDOWAGA" \
               "\nZmień swoje nawyki żywieniowe i zadbaj o zdrowie"
    elif 18.5 <= bmi <= 22.99:
        return "BRAWO! JEST DOBRZE :)" \
               "\nPamiętaj o posiłkach, a zachowasz dobry wskaźnik ;)"
    elif 23 <= bmi <= 24.99:
        return "BRAWO! JEST DOBRZE :)" \
               "\nUważaj na kalorie, by zachować dobry wskaźnik ;)"
    elif 25 <= bmi <= 27.49:
        return "Lekka nadwaga" \
               "\nZmień swoje nawyki żywieniowe i zadbaj o zdrowie"
    elif 27.5 <= bmi <= 29.99:
        return "Wyraźna NADWAGA" \
               "\nZmień swoje nawyki żywieniowe, trochę ruchu i zadbaj o zdrowie"
    elif 30 <= bmi <= 34.99:
        return "Ups... Twoje BMI wskazuje na otyłość I stopnia" \
               "\nZachęcamy do poszukania pomocy"
    elif 35 <= bmi <= 39.99:
        return "Jest ŹLE!" \
               "\nTwoje BMI wskazuje na otyłość II stopnia" \
               "\nPotrzebujesz lekarza :("
    elif bmi >= 40:
        return ":( OJEJ  Cierpisz na otyłość III stopnia! " \
               "\nStanowczo potrzebna pomoc medyczna! :("
    else:
        return "Coś poszło nie tak. Sprawdź wprowadzone dane."

def oblicz_i_pokaz_bmi():
    imie = entry_imie.get()
    waga = entry_waga.get()
    wzrost = entry_wzrost.get()

    try:
        bmi_wynik = oblicz_bmi(waga, wzrost)
        now = datetime.datetime.now()
        current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

        result_message = f"Imię: {imie}\nBMI: {bmi_wynik}\n{interpretuj_bmi(bmi_wynik)}\nData i godzina: {current_datetime}"

        messagebox.showinfo("BMI", result_message)

        root.print_result = result_message
        button_drukuj["state"] = "normal"

    except ValueError as e:
        messagebox.showerror("Błąd", f"Błąd: {e}")

def drukuj_wynik():
    try:
        if root.print_result:
            confirmed = messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz zapisać wynik do pliku?")
            if confirmed:

                filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

                if filename:

                    with open(filename, "w") as file:
                        file.write(root.print_result)

                    messagebox.showinfo("Sukces", "Wynik został pomyślnie zapisany.")

                    root.after(100, lambda: open_in_default_editor(filename))

                
                root.print_result = None
                button_drukuj["state"] = "disabled"  # Zablokowanie przycisku
    except Exception as e:
        messagebox.showerror("Błąd", f"Błąd podczas zapiszwania: {e}")


def open_in_default_editor(filename):
    import subprocess
    subprocess.run(["start", "", filename], shell=True)


root = tk.Tk()
root.title("Kalkulator BMI")

label_imie = tk.Label(root, text="Podaj imię:")
label_imie.pack()

entry_imie = tk.Entry(root)
entry_imie.pack()

label_waga = tk.Label(root, text="Podaj wagę (kg):")
label_waga.pack()

entry_waga = tk.Entry(root)
entry_waga.pack()

label_wzrost = tk.Label(root, text="Podaj wzrost (cm):")
label_wzrost.pack()

entry_wzrost = tk.Entry(root)
entry_wzrost.pack()

button_oblicz = tk.Button(root, text="Oblicz BMI", command=oblicz_i_pokaz_bmi)
button_oblicz.pack()

button_drukuj = tk.Button(root, text="Zapisz do pliku tekstowego", command=drukuj_wynik, state="disabled")
button_drukuj.pack()

root.geometry("400x200")
root.mainloop()
