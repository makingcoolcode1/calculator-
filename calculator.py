
from tkinter import *

def insert_numbers(value):
    number_text = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, number_text + value)

def calculate():

    try:
        execute = entry_field.get()
        entry_field.delete(0, END)
        entry_field.insert(0, eval(str(execute)))
    
    except Exception as e:
        entry_field.delete(0, END)
        entry_field.insert(0, str(e))

def clear_screen():
    entry_field.delete(0, END)



root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(0,0)


entry_field = Entry(root, width=30)
entry_field.grid(row=0, column=0, columnspan=4)

numbers = [

    ("9", 1, 0), ("8", 1, 1), ("7", 1, 2), ("+", 1, 3), 
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2), ("-", 2, 3), 
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("*", 3, 3)

]

for text, row, col in numbers:
    main_buttons = Button(root, text=text, command=lambda value=text: insert_numbers(value) if entry_field != "=" else calculate)
    main_buttons.grid(row=row, column=col, sticky=NSEW)

equals_btn = Button(root, text="=", command=calculate)
equals_btn.grid(row=4, column=0, sticky=NSEW, columnspan=4)

clear_btn = Button(root, text="C", width=5, command=clear_screen)
clear_btn.grid(row=0, column=3)


for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)


root.mainloop()