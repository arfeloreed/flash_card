import tkinter as tk
import pandas
import random as rn
# constant
BACKGROUND_COLOR = "#B1DDC6"
# global
french_word = {}
try:
    new_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    old_data = pandas.read_csv("./data/french_words.csv")
    french_dict = pandas.DataFrame.to_dict(old_data, orient="records")
except pandas.errors.EmptyDataError:
    old_data = pandas.read_csv("./data/french_words.csv")
    french_dict = pandas.DataFrame.to_dict(old_data, orient="records")
else:
    french_dict = pandas.DataFrame.to_dict(new_data, orient="records")


def x_word():
    """returns a random French word"""
    global french_word, timer
    window.after_cancel(timer)
    french_word = rn.choice(french_dict)
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(text_word, text=f"{french_word['French']}", fill="black")
    timer = window.after(3000, func=flip)


def flip():
    """flips the card to the other side after 3 seconds"""
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=f"{french_word['English']}", fill="white")


def check_word():
    """creates a new dictionary and a new csv file named words to learn"""
    french_dict.remove(french_word)
    new_dict = pandas.DataFrame(french_dict)
    new_dict.to_csv("./data/words_to_learn.csv", index=False)
    x_word()


# make the ui
window = tk.Tk()
window.title("French Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip)

# import images
image_front = tk.PhotoImage(file="./images/card_front.png")
image_back = tk.PhotoImage(file="./images/card_back.png")
image_right = tk.PhotoImage(file="./images/right.png")
image_wrong = tk.PhotoImage(file="./images/wrong.png")

# create canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=image_front)
text_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create button
button_x = tk.Button(image=image_wrong, highlightthickness=0, command=x_word)
button_x.grid(row=1, column=0)
button_check = tk.Button(image=image_right, highlightthickness=0, command=check_word)
button_check.grid(row=1, column=1)

x_word()
window.mainloop()
