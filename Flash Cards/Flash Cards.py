from dataclasses import Field

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
def next_word(right_or_wrong):
    global random_word
    if right_or_wrong == 'right':
        try:
            updated_words = pandas.read_csv(r'data\words_to_learn.csv')
            updated_words = updated_words[updated_words['French'] != random_word['French']]
            updated_words.to_csv(r'data\words_to_learn.csv',index=False)
        except FileNotFoundError:
            old_words = pandas.read_csv(csv_location)
            old_words = old_words[old_words['French'] != random_word['French']]
            old_words.to_csv(r'data\words_to_learn.csv',index=False)
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(language,text='French',fill='black')
    random_word = random.choice(french_dict)
    canvas.itemconfig(word_language,text=random_word['French'],fill='black')
    window.after(3000,flip)
def flip():
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(language,text='English',fill='white')
    canvas.itemconfig(word_language,text=random_word['English'],fill='white')
csv_location = r'data\french_words.csv'
try:
    french = pandas.read_csv(r'data\words_to_learn.csv')
except FileNotFoundError:
    french = pandas.read_csv(csv_location)
french_dict = french.to_dict(orient='records')
random_word = random.choice(french_dict)
window = Tk()
window.title('Flashy')
window.minsize(1200,800)
window.config(bg=BACKGROUND_COLOR)
canvas = Canvas(window,width= 800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file=r'images\card_front.png')
card_back = PhotoImage(file=r'images\card_back.png')
canvas_image = canvas.create_image(400,263,image=card_front)
language = canvas.create_text(400,150,text='French',font=('Ariel',40,'italic'))
word_language = canvas.create_text(400,263,text=random_word['French'],font=('Ariel',60,'bold'))
canvas.place(x=200,y=50)
wrong = PhotoImage(file=r'images\wrong.png')
wrong_button = Button(image=wrong,command=lambda: next_word("wrong"))
wrong_button.place(x=320,y=600)
right = PhotoImage(file=r'images\right.png')
right_button = Button(image=right,command=lambda: next_word("right"))
right_button.place(x=750,y=600)
window.after(3000,flip)
window.mainloop()
