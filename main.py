import tkinter
from cgitb import reset
from  tkinter import*
import winsound

import math


PINK = "#E2979C"
RED = "E7305B"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text = "Timer",fg ="#9FC87E", bg ="#cfe3e4", font = ("Fixedsys", 24, "bold"))
    check_mark.config(text = "")
    global reps
    reps = 0



#timer_m
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text = "Break",fg = RED,font = ("Fixedsys",20,"bold"))
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text = "Break",fg = PINK, font = ("Fixedsys",20,"bold"))

    else:
        count_down(work_sec)
        title_label.config(text = "WORK",fg = GREEN,font = ("Fixedsys",20,"bold"))




#constant
import time

def count_down(count):

    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer =  window.after(1000, count_down,count - 1)
    else:
        import winsound
        import time
        for _ in range(3):
            winsound.Beep(1200, 300)
            time.sleep(0.3)
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            mark +=  "✅"
        check_mark.config(text = mark)



# UI

from tkinter import *
from tkinter import font

window = Tk()
window.title("FocusUp")

window.config(padx=0, pady=0, bg="#cfe3e4")



title_label = Label(text = "TIMER", fg ="#9FC87E", bg ="#cfe3e4", font = ("Fixedsys", 24, "bold"))
title_label.grid(column = 1, row = 0)
# Load the image
BG_image = PhotoImage(file="assets/BG_cute.png")
canvas = Canvas(width=250, height=250, highlightthickness=0, bg="#cfe3e4")
canvas.create_image(120, 111, image= BG_image)
timer_text = canvas.create_text(122, 200, text="00:00", fill="black", font=("Courier", 24, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=("Fixedsys", 15),
                         bg="#cfe3e4", fg="black", highlightthickness=0, bd=0, activebackground="#bcd5d6", command = start_timer)
start_button.grid(column = 0, row = 2)
reset_button = Button(text="Reset", font=("Fixedsys", 15),
                         bg="#cfe3e4", fg="black", highlightthickness=0, bd=0, activebackground="#bcd5d6", command = reset_timer
)
reset_button.grid(column = 2, row= 2)


check_mark = Label( fg = GREEN, bg="#cfe3e4", font = ("arial",20,"bold"))
check_mark.grid(column = 1 , row  = 3)




window.mainloop()
