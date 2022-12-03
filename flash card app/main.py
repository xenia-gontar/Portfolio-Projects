from tkinter import *
import pandas

vocab = pandas.read_csv("vocab.csv")

window = Tk()
window.config(width=600, height=500, padx=20, pady=20)

#Simple GUI

current_card = Label(text="Word")
current_card.grid(row=0, column=1)

no_button = Button(text="I don't know this word")
no_button.grid(row=1, column=0)

flip_button = Button(text="Show translation")
flip_button.grid(row=1, column=1)

yes_button = Button(text="I know this word")
yes_button.grid(row=1, column=2)


window.mainloop()
