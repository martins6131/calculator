import tkinter as tk
from math import sqrt

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.config(bg="#1e1e1e")

# Display entry
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
display.pack(pady=10, padx=10, fill="x")

# Function to append values
def append_value(value):
    display.insert(tk.END, value)

# Function to clear display
def clear_display():
    display.delete(0, tk.END)

# Function to delete last character
def delete_last():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Function to calculate
def calculate():
    try:
        expression = display.get().replace("%", "/100")
        result = eval(expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")

# Square root
def square_root():
    try:
        result = sqrt(float(display.get()))
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")

# Square
def square():
    try:
        result = float(display.get()) ** 2
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")

# Button layout
buttons = [
    ("C", clear_display), ("DEL", delete_last), ("%", lambda: append_value("%")), ("/", lambda: append_value("/")),
    ("7", lambda: append_value("7")), ("8", lambda: append_value("8")), ("9", lambda: append_value("9")), ("*", lambda: append_value("*")),
    ("4", lambda: append_value("4")), ("5", lambda: append_value("5")), ("6", lambda: append_value("6")), ("-", lambda: append_value("-")),
    ("1", lambda: append_value("1")), ("2", lambda: append_value("2")), ("3", lambda: append_value("3")), ("+", lambda: append_value("+")),
    ("0", lambda: append_value("0")), (".", lambda: append_value(".")), ("√", square_root), ("x²", square),
    ("=", calculate)
]

# Create buttons dynamically
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

row, col = 0, 0
for text, command in buttons:
    btn = tk.Button(frame, text=text, width=6, height=2, font=("Arial", 14),
                    command=command, bg="#444", fg="white", activebackground="#666")
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
