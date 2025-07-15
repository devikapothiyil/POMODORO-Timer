import tkinter as tk
from tkinter import PhotoImage
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds =LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_minute= math.floor(count / 60)
    count_seconds=count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text,text= f"{count_minute}:{count_seconds}")
    if count > 0:
        timer = root.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor( reps/2)
        for _ in  range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

root=tk.Tk()
root.title("Pomodoro")
root.config(padx=100,pady=50,bg=YELLOW)

canvas = tk.Canvas(root,width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,135,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=2,row=2)

timer_label=tk.Label(root,text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=2,row=1)

start_button=tk.Button(root,text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)

reset_button=tk.Button(root,text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)

checkmark=tk.Label(root,fg=GREEN,bg=YELLOW)
checkmark.grid(column=2,row=4)

root.mainloop()
