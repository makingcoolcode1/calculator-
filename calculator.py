
from tkinter import *

def button_click(value):
    click = main_entry.get()
    main_entry.delete(0, END)
    main_entry.insert(0, click + value)

def calculate():
    result = eval(main_entry.get())
    main_entry.delete(0, END)
    main_entry.insert(0, str(result))



root = Tk()
root.title("Calculator")
root.geometry("500x500")
root.resizable(0,0)


main_entry = Entry(root, width=20, font=('verdana', 18))
main_entry.grid(row = 0, column=0, columnspan=4)


buttons = [

    ("9", 1, 0), ("8", 1, 1), ("7", 1, 2), ('+', 1, 3),
    ("6", 2, 0), ("5", 2, 1, ), ("4", 2, 2), ("-", 2,3),
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("*", 3, 3, ), 
    ("0", 4, 0), ("%", 4, 1), ("/", 4, 2), (".", 4, 3)
]

for (text, row, col) in buttons:

    main_buttons = Button(root, text=text, padx=20, pady=20, command=lambda value = text: button_click(value) if value != "" else calculate())
    main_buttons.grid(row = row, column=col, sticky=NSEW)

equals_button = Button(root, text="=", font=('arial', 12), command=calculate)
equals_button.grid(row = 5,column=0, columnspan=4)


for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

root.mainloop()

