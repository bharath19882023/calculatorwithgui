import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate(num1, num2, operation, user_name):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values.")
        return

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return
        else:
            result = num1 / num2
    else:
        result = "Invalid operation selected."
    messagebox.showinfo("Result", f"The result is: {result}")

def main_app():
    root = tk.Tk()
    root.withdraw()  # Hides the main window

    user_name = simpledialog.askstring("Name", "Please enter your name:")
    if user_name:
        messagebox.showinfo("Welcome", f"Hello, {user_name}! Welcome to the Calculator Program.")
    
    while True:
        num1 = simpledialog.askstring("Input", "Enter first number:")
        num2 = simpledialog.askstring("Input", "Enter second number:")
        operation = simpledialog.askstring("Operation", "Choose the operation (Addition, Subtraction, Multiplication, Division):")
        
        if not all([num1, num2, operation]):
            break  # Exit if any of the inputs are missing

        calculate(num1, num2, operation, user_name)

        if not messagebox.askyesno("Continue", "Do you want to perform another calculation?"):
            break

    messagebox.showinfo("Goodbye", f"Goodbye, {user_name}. {user_name}, visit again.")

if __name__ == "__main__":
    main_app()
