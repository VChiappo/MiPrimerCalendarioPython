import tkinter as tk
from tkcalendar import Calendar

def print_date():
    print(cal.selection_get())

root = tk.Tk()
root.title("Calendario")

cal = Calendar(root, selectmode='day', year=2024, month=6, day=2)
cal.pack(pady=20)

tk.Button(root, text='Seleccionar fecha', command=print_date).pack(pady=20)  # Corrected here

root.mainloop()
