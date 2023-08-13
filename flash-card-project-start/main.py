BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
try:
    words = pd.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient='records')
else:
    words = words.to_dict('records')
from tkinter import *

chosen_french= {}

def next_card():
    global chosen_french, flip_timer
    window.after_cancel(flip_timer)
    chosen_french = random.choice(words)
    canvas.itemconfig(image_front, image=my_image)
    canvas.itemconfig(french_title, text='French', fill='black')
    canvas.itemconfig(french_text, text=chosen_french["French"], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(image_front,image= my_card_back)
    canvas.itemconfig(french_title, text="English",fill='white')
    canvas.itemconfig(french_text, text =chosen_french['English'], fill='white')

def is_known():
    words.remove(chosen_french)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn", index=False)
    next_card()



window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
my_card_back= PhotoImage(file=r"C:\Users\jagya\Downloads\flash-card-project-start\images\card_back.png")
my_image = PhotoImage(file=r"C:\Users\jagya\Downloads\flash-card-project-start\images\card_front.png")
image_front = canvas.create_image(400, 263, image=my_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
french_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
french_text = canvas.create_text(400, 300, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file=r"C:\Users\jagya\Downloads\flash-card-project-start\images\right.png")
correct = Button(image=correct_img, highlightthickness=0,command=is_known)
correct.grid(row=5, column=1)

wrong_img = PhotoImage(file=r"C:\Users\jagya\Downloads\flash-card-project-start\images\wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong.grid(row=5, column=0)

next_card()
window.mainloop()


