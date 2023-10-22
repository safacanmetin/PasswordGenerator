import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    password = ""
    length = int(length_var.get())
    
    if small_letters_var.get():
        password += string.ascii_lowercase
    if capital_letters_var.get():
        password += string.ascii_uppercase
    if symbols_var.get():
        password += string.punctuation
    
    if len(password) == 0:
        password_label.config(text="Please select at least one complexity level.")
        return
    
    password = ''.join(random.choice(password) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_label.config(text="Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

length_label = tk.Label(frame, text="Password Length:")
length_label.pack()

length_var = tk.StringVar()
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.pack()

small_letters_var = tk.BooleanVar()
small_letters_checkbox = ttk.Checkbutton(frame, text="Small Letters", variable=small_letters_var)
small_letters_checkbox.pack()

capital_letters_var = tk.BooleanVar()
capital_letters_checkbox = ttk.Checkbutton(frame, text="Capital Letters", variable=capital_letters_var)
capital_letters_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(frame, text="Symbols", variable=symbols_var)
symbols_checkbox.pack()

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack()

password_entry = ttk.Entry(frame)
password_entry.pack()

password_label = ttk.Label(frame, text="")
password_label.pack()

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=lambda: pyperclip.copy(password_entry.get()))
copy_button.pack()

root.update()
frame_width = frame.winfo_width()
frame_height = frame.winfo_height()
x = (root.winfo_screenwidth() // 2) - (frame_width // 2)
y = (root.winfo_screenheight() // 2) - (frame_height // 2)
root.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x, y))

root.geometry("300x300")

root.mainloop()
