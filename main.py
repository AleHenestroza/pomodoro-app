# ----------------------------- IMPORTS -------------------------------- #
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ----------------------------- #
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    pomodoro_count_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------- #
def start_timer():
    global reps
    reps += 1

    pomodoro_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(pomodoro_secs)
        label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_secs)
        label.config(text="Break", fg=RED)
    else:
        countdown(short_break_secs)
        label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def countdown(count):
    global reps

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"

        label.config(text=marks)


# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Pomodoro App - by Ale Henestroza")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="./tomato.png")

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

pomodoro_count_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
pomodoro_count_label.grid(column=1, row=3)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

pomodoro_count_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
pomodoro_count_label.grid(column=1, row=3)

window.mainloop()
