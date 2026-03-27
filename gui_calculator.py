import tkinter as tk

# Functions
def calculate_current():
    label1.config(text="Voltage (V)")
    label2.config(text="Resistance (Ohms)")
    result_label.config(text="Enter values above")

    try:
        V = float(entry1.get())
        R = float(entry2.get())
        result = V / R
        result_label.config(text="Current = " + str(round(result, 2)) + " A")
    except ValueError:
        result_label.config(text="Enter numbers only")
    except ZeroDivisionError:
        result_label.config(text="Resistance cannot be zero")


def calculate_voltage():
    label1.config(text="Current (A)")
    label2.config(text="Resistance (Ohms)")
    result_label.config(text="Enter values above")

    try:
        I = float(entry1.get())
        R = float(entry2.get())
        result = I * R
        result_label.config(text="Voltage = " + str(round(result, 2)) + " V")
    except ValueError:
        result_label.config(text="Enter numbers only")


def calculate_resistance():
    label1.config(text="Voltage (V)")
    label2.config(text="Current (A)")
    result_label.config(text="Enter values above")

    try:
        V = float(entry1.get())
        I = float(entry2.get())
        result = V / I
        result_label.config(text="Resistance = " + str(round(result, 2)) + " Ohms")
    except ValueError:
        result_label.config(text="Enter numbers only")
    except ZeroDivisionError:
        result_label.config(text="Current cannot be zero")


def calculate_power():
    label1.config(text="Voltage (V)")
    label2.config(text="Current (A)")
    result_label.config(text="Enter values above")

    try:
        V = float(entry1.get())
        I = float(entry2.get())
        result = V * I
        result_label.config(text="Power = " + str(round(result, 2)) + " Watts")
    except ValueError:
        result_label.config(text="Enter numbers only")


# Window
window = tk.Tk()
window.title("Electrical Calculator")
window.geometry("320x400")

# Title
title = tk.Label(window, text="Electrical Calculator", font=("Arial", 14))
title.pack(pady=10)

# Input labels and fields
label1 = tk.Label(window, text="Select a calculation")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window, text="")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Buttons
tk.Button(window, text="Calculate Current", command=calculate_current).pack(pady=5)
tk.Button(window, text="Calculate Voltage", command=calculate_voltage).pack(pady=5)
tk.Button(window, text="Calculate Resistance", command=calculate_resistance).pack(pady=5)
tk.Button(window, text="Calculate Power", command=calculate_power).pack(pady=5)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=15)

# Run app
window.mainloop()