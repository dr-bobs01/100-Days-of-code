from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20,)

#Labels
labelL = Label(text="is equal to")
labelL.grid(column=0, row=1)

labelM = Label(text=0)
labelM.grid(column=1, row=1)

labelR1 = Label(text="Miles")
labelR1.grid(column=2, row=0)
labelR2 = Label(text="Km")
labelR2.grid(column=2, row=1)

#Buttons
def action():
    labelM["text"] = round((int(entry.get()) * 1.609), 1)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)


window.mainloop()
