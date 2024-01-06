
from tkinter import *

def button_press(value):
    current = entry_window.get()
    entry_window.delete(0, END)
    entry_window.insert(0, current + value)

def calculate():
    try:
        calc = entry_window.get()
        entry_window.delete(0, END)
        entry_window.insert(0, eval(str(calc)))
    except Exception as e:
        entry_window.delete(0, END)
        entry_window.insert(0, f"ERROR: {str(e)}")


root = Tk()
root.title("Calculator")
root.geometry('600x600')
root.resizable(0,0)


entry_window = Entry(root, width=30, font=('verdana', 18))
entry_window.grid(row = 0, column=0, columnspan=4)

buttons = [
    ("9", 1,0), ("8", 1, 1), ("7", 1, 2), ("+", 1, 3), 
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2), ("-", 2, 3), 
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("*", 3, 3), 
    ("/", 4, 0), (".", 4, 1), ("%", 4, 2), ("$", 4, 3)  
]


for (text, row, col) in buttons:

    main_buttons = Button(root, text=text, command = lambda value  = text:button_press(value) if value !="=" else calculate())
    main_buttons.grid(row = row, column=col, sticky=NSEW)

equels_button = Button(root, text="=", width=20 ,command=calculate)
equels_button.grid(row = 5, column=0, columnspan=4, sticky=NSEW)

for i in range(6):
    root.columnconfigure(i, weight=2)
    root.rowconfigure(i, weight=2)



root.mainloop()