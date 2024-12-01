import tkinter as tk
from tkinter import ttk
from datetime import datetime

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = datetime(year, month, day)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Hello {name}, you are {age} years old.")
    except ValueError:
        result_label.config(text="Please enter valid date values.")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

ttk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Day:").grid(row=1, column=0, padx=10, pady=10)
day_entry = ttk.Entry(root)
day_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Month:").grid(row=2, column=0, padx=10, pady=10)
month_entry = ttk.Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(root, text="Year:").grid(row=3, column=0, padx=10, pady=10)
year_entry = ttk.Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
