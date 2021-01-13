from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------- LOAD DATA ----------------------------- #

try:
    word_data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    word_data = pd.read_csv("./data/french_words.csv")

to_learn = word_data.to_dict(orient="records")
current_card = {}

# -------------------------- FLASH CARD ----------------------------- #


def update_words():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, fill="black", text="French")
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# set buttons
correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=update_words)
correct_button.config(padx=50, pady=50)
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.config(padx=50, pady=50)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
