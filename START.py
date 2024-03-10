import tkinter as tk
from tkinter import messagebox
import os

def run_script(script_name):
    os.system(f"python {script_name}")

def choose_language(language):
    if language == "Polski":
        run_script("PL_BMI.py")
    elif language == "English":
        run_script("EN_BMI.py")
    elif language == "Deutsch":
        run_script("DE_BMI.py")
    else:
        messagebox.showerror("Error", "Invalid language selection")

def language_menu():
    root = tk.Tk()
    root.title("Choose Language")

    label = tk.Label(root, text="CHOOSE LANGUAGE", font=("Helvetica", 16))
    label.pack(pady=20)

    def on_button_click(language):
        choose_language(language)
        root.destroy()

    button_pl = tk.Button(root, text="POLSKI", command=lambda: on_button_click("Polski"))
    button_en = tk.Button(root, text="ENGLISH", command=lambda: on_button_click("English"))
    button_de = tk.Button(root, text="DEUTSCH", command=lambda: on_button_click("Deutsch"))

    button_pl.pack()
    button_en.pack()
    button_de.pack()

    root.mainloop()

if __name__ == "__main__":
    language_menu()

