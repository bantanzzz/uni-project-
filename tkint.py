import tkinter as tk
from tkinter import messagebox
from tkinter import font



def convert():
    binary = entry.get()

    try:
        decimal = int(binary, 2)
        hex_value = hex(decimal)[2:].upper()
        octal_value = oct(decimal)[2:]

        decimal_label.config(text=f"Decimal: {decimal}")
        hex_label.config(text=f"Hexadecimal: {hex_value}")
        octal_label.config(text=f"Octal: {octal_value}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid binary number")

app = tk.Tk()
app.title("LIMKOKWING CONVETER")
app.configure(bg='black')

bold_font = font.Font(family="Helvetica", size=30, weight="bold")



label = tk.Label(text="LIMKOKWING UNIVERSITY", font=bold_font)
label.pack(pady=30)

entry_label = tk.Label(app, text="Enter Binary Number:", bg='black', fg='white' , font=10)
entry_label.pack(pady=30)

entry = tk.Entry(app, bg='white', fg='black', width=30)
entry.pack(pady=30)

convert_button = tk.Button(app, text="Convert", command=convert, bg='red', fg='white')
convert_button.pack(pady=30)

decimal_label = tk.Label(app, text="Decimal: ", bg='black', fg='white' , font=10)
decimal_label.pack(pady=5)

hex_label = tk.Label(app, text="Hexadecimal: ", bg='black', fg='white' , font=10)
hex_label.pack(pady=5)

octal_label = tk.Label(app, text="Octal: ", bg='black', fg='white' , font=10)
octal_label.pack(pady=5)

app.mainloop()