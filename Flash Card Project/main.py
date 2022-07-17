import os
from tkinter import *
import pandas as p
import random
import time

os.system('cls')
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}
# ---------------------------- FUNCTIONS ------------------------------- #


try:
    data = p.read_csv("Flash Card Project/data/words to learn.csv")
except FileNotFoundError:
    original_data = p.read_csv("Flash Card Project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")
# print(data_dict)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(img, image=fcard_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(img, image=fcard_back_img)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = p.DataFrame(to_learn)
    data.to_csv("Flash Card Project/data/words to learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
#window.minsize(height=600, width=900)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
fcard_front_img = PhotoImage(file="Flash Card Project/images/card_front.png")
fcard_back_img = PhotoImage(file="Flash Card Project/images/card_back.png")
img = canvas.create_image(400, 263, image=fcard_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_LANG)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file="Flash Card Project/images/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="Flash Card Project/images/right.png")
right_button = Button(
    image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
