# CODED BY: Kamil Sulewski
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

def calculate_bmi(weight, height):
    weight2 = weight.replace(",", ".")
    height2 = height.replace(",", ".")

    try:
        weight_float = float(weight2)
        height_float = float(height2)

        if weight_float > 0 and height_float > 0:
            bmi_result = weight_float / ((height_float * 0.01) ** 2)
            return round(bmi_result, 2)
        else:
            raise ValueError("Weight and height values must be positive.")
    except ValueError as e:
        raise e

def interpret_bmi(bmi):
    if 16 > bmi > 0:
        return "OH NO! Your BMI indicates severe underweight :(" \
               "\nWe recommend contacting medical assistance quickly!"
    elif 16 <= bmi <= 16.99:
        return "Oops... Your BMI suggests underweight :(" \
               "\nConsider seeking help."
    elif 17 <= bmi <= 18.49:
        return "UNDERWEIGHT" \
               "\nChange your eating habits and take care of your health."
    elif 18.5 <= bmi <= 22.99:
        return "WELL DONE! IT'S GOOD :)" \
               "\nRemember to have balanced meals to maintain a good index ;)"
    elif 23 <= bmi <= 24.99:
        return "WELL DONE! IT'S GOOD :)" \
               "\nWatch your calorie intake to maintain a good index ;)"
    elif 25 <= bmi <= 27.49:
        return "Slight overweight" \
               "\nChange your eating habits and take care of your health."
    elif 27.5 <= bmi <= 29.99:
        return "Significant OVERWEIGHT" \
               "\nChange your eating habits, get some exercise, and take care of your health."
    elif 30 <= bmi <= 34.99:
        return "Oops... Your BMI indicates obesity I degree" \
               "\nConsider seeking help."
    elif 35 <= bmi <= 39.99:
        return "IT'S BAD!" \
               "\nYour BMI indicates obesity II degree" \
               "\nYou need a doctor :("
    elif bmi >= 40:
        return ":(" \
               "\nYou suffer from obesity III degree!" \
               "\nUrgent medical help is needed! :("
    else:
        return "Something went wrong. Check the entered data."

def calculate_and_show_bmi():
    name = entry_name.get()
    weight = entry_weight.get()
    height = entry_height.get()

    try:
        bmi_result = calculate_bmi(weight, height)
        now = datetime.datetime.now()
        current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

        result_message = f"Name: {name}\nBMI: {bmi_result}\n{interpret_bmi(bmi_result)}\nDate and time: {current_datetime}"

        messagebox.showinfo("BMI", result_message)

        root.print_result = result_message
        button_print["state"] = "normal"

    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")

def print_result():
    try:
        if root.print_result:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to save the result to a text file?")
            if confirmed:

                filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

                if filename:

                    with open(filename, "w") as file:
                        file.write(root.print_result)

                    messagebox.showinfo("Success", "The result has been successfully saved.")

                    root.after(100, lambda: open_in_default_editor(filename))

                
                root.print_result = None
                button_print["state"] = "disabled"  # Disable the button
    except Exception as e:
        messagebox.showerror("Error", f"Error during saving: {e}")


def open_in_default_editor(filename):
    import subprocess
    subprocess.run(["start", "", filename], shell=True)


root = tk.Tk()
root.title("BMI Calculator")

label_name = tk.Label(root, text="Enter name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_weight = tk.Label(root, text="Enter weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text="Enter height (cm):")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_and_show_bmi)
button_calculate.pack()

button_print = tk.Button(root, text="Save to text file", command=print_result, state="disabled")
button_print.pack()

root.geometry("400x200")
root.mainloop()

