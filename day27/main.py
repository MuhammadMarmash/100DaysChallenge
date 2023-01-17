from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)

entry = Entry()
entry.grid(row=0, column=1)

Label(text="Miles").grid(row=0, column=2)
Label(text="is equal to").grid(row=1, column=0)
Label(text="Km").grid(row=1, column=2)
result = Label(text="")
result.grid(row=1, column=1)


def calculate():
    result.config(text=round(float(entry.get()) * 1.609))


btn = Button(text="Calculate", command=calculate)
btn.grid(row=3, column=1)

window.mainloop()
