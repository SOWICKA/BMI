# PROGRAMMIERT VON: Kamil Sulewski
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

def bmi_berechnen(gewicht, größe):
    gewicht2 = gewicht.replace(",", ".")
    größe2 = größe.replace(",", ".")

    try:
        gewicht_float = float(gewicht2)
        größe_float = float(größe2)

        if gewicht_float > 0 and größe_float > 0:
            bmi_ergebnis = gewicht_float / ((größe_float * 0.01) ** 2)
            return round(bmi_ergebnis, 2)
        else:
            raise ValueError("Die Gewichts- und Größenwerte müssen positiv sein.")
    except ValueError as e:
        raise e

def bmi_interpretieren(bmi):
    if 16 > bmi > 0:
        return "OH NEIN, Ihr BMI zeigt extreme Unterernährung an :(" \
               "\nWir empfehlen einen schnellen Kontakt mit medizinischer Hilfe!"
    elif 16 <= bmi <= 16.99:
        return "Hoppla... Ihr BMI zeigt Unterernährung an :(" \
               "\nWir empfehlen, Hilfe zu suchen"
    elif 17 <= bmi <= 18.49:
        return "UNTERGEWICHT" \
               "\nÄndern Sie Ihre Ernährungsgewohnheiten und kümmern Sie sich um Ihre Gesundheit"
    elif 18.5 <= bmi <= 22.99:
        return "GUT GEMACHT! ALLES IST IN ORDNUNG :)" \
               "\nDenken Sie an Mahlzeiten, um einen guten Wert zu erhalten ;)"
    elif 23 <= bmi <= 24.99:
        return "GUT GEMACHT! ALLES IST IN ORDNUNG :)" \
               "\nAchten Sie auf Kalorien, um einen guten Wert zu erhalten ;)"
    elif 25 <= bmi <= 27.49:
        return "Leichtes Übergewicht" \
               "\nÄndern Sie Ihre Ernährungsgewohnheiten und kümmern Sie sich um Ihre Gesundheit"
    elif 27.5 <= bmi <= 29.99:
        return "Deutliches Übergewicht" \
               "\nÄndern Sie Ihre Ernährungsgewohnheiten, etwas Bewegung und kümmern Sie sich um Ihre Gesundheit"
    elif 30 <= bmi <= 34.99:
        return "Hoppla... Ihr BMI zeigt Adipositas I an" \
               "\nWir empfehlen, Hilfe zu suchen"
    elif 35 <= bmi <= 39.99:
        return "ES IST SCHLECHT!" \
               "\nIhr BMI zeigt Adipositas II an" \
               "\nSie brauchen einen Arzt :("
    elif bmi >= 40:
        return ":( OH NEIN, Sie leiden unter Adipositas III! " \
               "\nDringend medizinische Hilfe erforderlich! :("
    else:
        return "Etwas ist schief gelaufen. Überprüfen Sie die eingegebenen Daten."

def bmi_berechnen_und_anzeigen():
    vorname = entry_vorname.get()
    gewicht = entry_gewicht.get()
    größe = entry_größe.get()

    try:
        bmi_ergebnis = bmi_berechnen(gewicht, größe)
        jetzt = datetime.datetime.now()
        aktuelle_zeit = jetzt.strftime("%Y-%m-%d %H:%M:%S")

        ergebnis_nachricht = f"Vorname: {vorname}\nBMI: {bmi_ergebnis}\n{bmi_interpretieren(bmi_ergebnis)}\nDatum und Uhrzeit: {aktuelle_zeit}"

        messagebox.showinfo("BMI", ergebnis_nachricht)

        root.print_result = ergebnis_nachricht
        button_drucken["state"] = "normal"

    except ValueError as e:
        messagebox.showerror("Fehler", f"Fehler: {e}")

def ergebnis_drucken():
    try:
        if root.print_result:
            bestätigt = messagebox.askyesno("Bestätigung", "Möchten Sie das Ergebnis wirklich in einer Textdatei speichern?")
            if bestätigt:

                dateiname = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])

                if dateiname:

                    with open(dateiname, "w") as datei:
                        datei.write(root.print_result)

                    messagebox.showinfo("Erfolg", "Das Ergebnis wurde erfolgreich gespeichert.")

                    root.after(100, lambda: in_standard_editor_öffnen(dateiname))

                
                root.print_result = None
                button_drucken["state"] = "disabled"  # Deaktivieren der Schaltfläche
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Speichern: {e}")


def in_standard_editor_öffnen(dateiname):
    import subprocess
    subprocess.run(["start", "", dateiname], shell=True)


root = tk.Tk()
root.title("BMI-Rechner")

label_vorname = tk.Label(root, text="Vorname eingeben:")
label_vorname.pack()

entry_vorname = tk.Entry(root)
entry_vorname.pack()

label_gewicht = tk.Label(root, text="Gewicht eingeben (kg):")
label_gewicht.pack()

entry_gewicht = tk.Entry(root)
entry_gewicht.pack()

label_größe = tk.Label(root, text="Größe eingeben (cm):")
label_größe.pack()

entry_größe = tk.Entry(root)
entry_größe.pack()

button_berechnen = tk.Button(root, text="BMI berechnen", command=bmi_berechnen_und_anzeigen)
button_berechnen.pack()

button_drucken = tk.Button(root, text="In Textdatei speichern", command=ergebnis_drucken, state="disabled")
button_drucken.pack()

root.geometry("400x200")
root.mainloop()

