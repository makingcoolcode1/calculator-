
from tkinter import *

def button_press(value):
    insert_number = entry_window.get()
    entry_window.delete(0, END)
    entry_window.insert(0, insert_number + value )

def calculate():
    try:
        calc_insert = entry_window.get()
        result = eval(str(calc_insert))
        entry_window.delete(0, END)
        entry_window.insert(0, result)
        print(result)

    except Exception as e:
        entry_window.delete(0, END)
        entry_window.insert(0, f"ERROR: {str(e)}")

def clear_screen():
    entry_window.delete(0, END)

root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(0,0)

entry_window = Entry(root, width=40, font=("arial", 12))
entry_window.grid(row=0, column=0, columnspan=4)

buttons = [

    ("9", 1, 0), ("8", 1, 1), ("7", 1, 2), ("+", 1, 3), 
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2), ("-", 2, 3), 
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("*", 3, 3)

]

for (text, row, col) in buttons:

    main_buttons = Button(root, text=text, font=("arial", 10), command=lambda value = text:button_press(value) if value!="=" else calculate())
    main_buttons.grid(row=row, column=col, sticky=NSEW)

    equals_button = Button(root, text="=" , font=("arial", 12), command=calculate)
    equals_button.grid(row=4, column=0, columnspan=4, sticky=NSEW)

    clear_button = Button(root, text="C", command=clear_screen)
    clear_button.grid(row=5, column=0, columnspan=4, sticky=NSEW)

    for i in range(6):
        root.columnconfigure(i, weight=2)
        root.rowconfigure(i, weight=4)
        
        

root.mainloop()