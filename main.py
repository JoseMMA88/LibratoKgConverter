from tkinter import *


def convert():
    label_4.config(text=str(float(input.get()) * 0.453592))


# Window Setup
window = Tk()
window.title("Libra to Kg Converter")
window.config(padx=20, pady=20)


# Setup labels
label = Label(text="Libras")
label.grid(column=2, row=0)

label_2 = Label(text="Kgs")
label_2.grid(column=2, row=1)

label_3 = Label(text="is equal to")
label_3.grid(column=0, row=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)

# Setup Textinput
input = Entry(width=7)
input.grid(column=1, row=0)

# Setup Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

# Window mainloop
window.mainloop()
