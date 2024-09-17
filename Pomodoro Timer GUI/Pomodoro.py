from turtledemo.penrose import start

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MIN = 25
sec = 60
rep = 0
loop = 0
text = 'Work'
lp = ''
from tkinter import *
def st():
    global MIN
    global sec
    global rep
    global loop
    global text
    global lp
    timer.config(text=text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
    sec -= 1
    if MIN == 0 and sec == 0:
        loop += 1
        if rep == 4:
            rep = 0
            text = 'Break'
            MIN = 30
        else:
            text = 'Break'
            MIN = 5
        if loop == 2:
            rep += 1
            loop = 0
            text = 'Work'
            MIN = 25
    if sec == 0:
        timer_break.config(text='{:02d}:{:02d}'.format(MIN, sec), fg='white', bg=RED, font=(FONT_NAME, 20))
        sec = 60
    elif sec == 59:
        MIN -= 1
        timer_break.config(text='{:02d}:{:02d}'.format(MIN, sec), fg='white', bg=RED, font=(FONT_NAME, 20))
    else:
        timer_break.config(text='{:02d}:{:02d}'.format(MIN, sec), fg='white', bg=RED, font=(FONT_NAME, 20))

    lp = window.after(1000, st)

def rt():
    global MIN
    global sec
    global rep
    global loop
    timer.config(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
    timer_break.config(text=f'00:00',fg='white',bg=RED,font=(FONT_NAME,20))
    MIN = 25
    sec = 60
    rep = 0
    loop = 0
    window.after_cancel(lp)


window =Tk()
window.title('Pomodoro Timer')
window.minsize(width=600,height=500)
window.configure(bg=YELLOW)
image = PhotoImage(file='tomato.png')
image_label = Label(image=image,bg=YELLOW)
image_label.place(x=200,y=140)
timer_break = Label(text=f'00:00',fg='white',bg=RED,font=(FONT_NAME,20))
timer_break.place(x=260,y=260)
start_button = Button(text='Start',command=st)
start_button.place(x=180,y=400)
reset_button = Button(text='Reset',command=rt)
reset_button.place(x=380,y=400)
timer = Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
timer.place(x=255,y=65)
window.mainloop()