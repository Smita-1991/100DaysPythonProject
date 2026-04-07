from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.5
work_cycle = 0
timer=None


# ---------------------------- TIMER RESET ------------------------------ #
def reset_timer():
    global work_cycle
    global timerReset
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    work_cycle=0

# ---------------------------- TIMER MECHANISM -------------------------- #
def start_timer():
    global work_cycle
    work_cycle += 1
    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60
    if work_cycle%8==0:
        title_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif work_cycle%2==0:
        title_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------ #
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
         timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(work_cycle/2)
        for _ in range(work_session):
            marks+="✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ----------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0, pady=(0, 20))

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    102, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill=YELLOW
)
canvas.grid(column=1, row=1, pady=(0, 20))

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3, pady=(20, 0))

window.mainloop()
