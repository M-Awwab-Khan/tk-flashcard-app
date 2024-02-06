BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *


window = Tk()
window.title('Flashcard Application')
window.config(bg='#B1DDC6', padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg='#B1DDC6', highlightthickness=0)
card_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_img)

canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
button = Button(image=correct_img, highlightthickness=0)
button.grid(row=1, column=0)

wrong_img = PhotoImage(file="./images/wrong.png")
button = Button(image=wrong_img, highlightthickness=0)
button.grid(row=1, column=1)

window.mainloop()
