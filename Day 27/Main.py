from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20,)

## Label

label = Label(text="This is a label", font=("Arial", 24, "bold"))
# label.pack()
## expand=True
## side="left"
# label.place(x=100,y=100)
label.grid(column=0, row=0)
## DONT MIX PACK AND GRID


label["text"] = "new text"
# label.config(text="new text")

## Button

def button_click():
    label["text"] = input.get()

button = Button(text="Button", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_click)
# button.pack()
new_button.grid(column=3, row=0)

## Entry

input = Entry(width=10)
# input.pack()
input.grid(column=4, row=3)
# input.get()








window.mainloop()
