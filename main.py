import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        return str(eval(expression, {"__builtins__": None}, math.__dict__))
    except Exception as e:
        return "Error"

# Function to handle button clicks
def button_click(value):
    current_expression = entry.get()
    current_expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, current_expression)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate and display the result
def calculate_result():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create an entry field for the expression
entry = tk.Entry(root, width=50, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Create buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin', 'cos', 'tan', 'sqrt',
    '(', ')', 'Clear', 'pi'
]

# Create buttons dynamically with larger size
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14),
                        command=calculate_result)
    elif button == 'Clear':
        btn = tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14),
                        command=clear_entry)
    else:
        btn = tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14),
                        command=lambda value=button: button_click(value))

    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Adjust grid weights for better resizing
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

for i in range(1, row_val + 1):
    root.grid_rowconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
