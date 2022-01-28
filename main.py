from tkinter import *
from random import choice, randint, shuffle

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
# CARD_BACK = PhotoImage(file='./images/card_back.png')


def wrong():
    pass


def right():
    pass


def main():
    display.mainloop()


display = Tk()
display.title('Flashy')
display.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

title_label = Label(text='Title', font=TITLE_FONT)
title_label.config(bg='white')
title_label.place(x=400, y=150)
# title_label.grid(column=0, row=0, padx=400, pady=150, columnspan=2)

word_label = Label(text='Word', font=WORD_FONT)
word_label.config(bg='white')
word_label.place(x=400, y=263)
# word_label.grid(column=0, row=0, columnspan=2, padx=400, pady=263)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(width=100, height=100, image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(width=100, height=100, image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)


if __name__ == '__main__':
    main()
