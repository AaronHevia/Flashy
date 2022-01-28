from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
MILLISECONDS = 3000

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('./data/Spanish-English_data.csv')

data_dict = data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, timer
    display.after_cancel(timer)
    current_card = choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text='Spanish', fill='black')
    canvas.itemconfig(word, text=current_card['Spanish'], fill='black')
    timer = display.after(MILLISECONDS, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')


def known():
    data_dict.remove(current_card)
    next_card()


def main():
    global data_dict
    next_card()
    display.mainloop()
    pd.DataFrame(data_dict).to_csv('./data/words_to_learn.csv', index=False)


display = Tk()
display.title('Flashy')
display.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = display.after(MILLISECONDS, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text='', font=TITLE_FONT)
word = canvas.create_text(400, 263, text='', font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

unknown_img = PhotoImage(file='./images/wrong.png')
unknown_button = Button(width=100, height=100, image=unknown_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_img = PhotoImage(file='./images/right.png')
known_button = Button(width=100, height=100, image=known_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=known)
known_button.grid(column=1, row=1)


if __name__ == '__main__':
    main()
