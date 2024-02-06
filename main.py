BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

words = pd.read_csv('./data/french_words.csv')




def change_word():
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(word_lang, text='French', fill='black')
    random_index = random.randint(0, 100)
    random_word = words.iloc[random_index].values[0]
    canvas.itemconfig(word_text, text=random_word, fill='black')



window = Tk()
window.title('Flashcard Application')
window.config(bg='#B1DDC6', padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg='#B1DDC6', highlightthickness=0)

card_front_img = PhotoImage(file='./images/card_front.png')
card = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file='./images/card_back.png')


word_lang = canvas.create_text(400, 150, text='French', font=('SF Pro Display', 25, 'italic'))
word_text = canvas.create_text(400, 250, text='English', font=('SF Pro Display', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
button = Button(image=correct_img, highlightthickness=0, command=change_word)
button.grid(row=1, column=0)

wrong_img = PhotoImage(file="./images/wrong.png")
button = Button(image=wrong_img, highlightthickness=0, command=change_word)
button.grid(row=1, column=1)

window.mainloop()
