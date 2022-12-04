from tkinter import *
import pandas
import random

vocab = pandas.read_csv("vocab.csv")
words = vocab[vocab["status"] == 0]["word"]
new_words = words.to_list()
print(new_words)

current_word = ""

def randomise_words():
    word = random.choice(new_words)
    current_card.config(text=word)
    global current_word
    current_word = word

def remove_words(word):
    new_words.remove(word)

def show_translation():
    translation = vocab[vocab["word"] == current_word]["translation"]
    current_translation = translation.to_list()
    current_card.config(text=current_translation)





window = Tk()
window.config(width=600, height=500, padx=20, pady=20)

# Simple GUI

current_card = Label(text="Word")
current_card.grid(row=0, column=1)

no_button = Button(text="I don't know this word")
no_button.grid(row=1, column=0)

flip_button = Button(text="Show translation", command=show_translation)
flip_button.grid(row=1, column=1)

yes_button = Button(text="I know this word")
yes_button.grid(row=1, column=2)

randomise_words()

window.mainloop()
