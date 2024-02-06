BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *


window = Tk()
window.title('Flashcard Application')
window.config(bg='#B1DDC6', padx=50, pady=50)

card = Canvas(width=800, height=526)
card.grid(row=0, column=0, columnspan=2)


window.mainloop()
