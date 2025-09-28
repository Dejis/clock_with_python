import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Clock label
clock_label = tk.Label(root, font=('Arial', 40), background='black', foreground='white')
clock_label.pack(anchor='center')

# Update function
def update_time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Start clock
update_time()
root.mainloop()
