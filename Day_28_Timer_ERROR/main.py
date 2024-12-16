from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

from Day_28_Timer_ERROR.times_breaks import TimeBreaks

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# 25 , 5(B) , 25 , 5(B) , 25 , 5(B) ,25, 20(LB)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW,padx=100,pady=50)

timer = TimeBreaks()




button_start =Button(text='Start')
button_reset =Button(text='Reset')
button_start.grid(column=0,row=2)
button_reset.grid(column=2,row=2)

check_mark = Label(text='✅',fg=GREEN,bg=YELLOW,font=('Arial',10))
check_mark.grid(column=1,row=3)

canvas = Canvas(bg=YELLOW,highlightthickness=0,width=200,height=224)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_png)
time= canvas.create_text(100,130,text='00:00',font=('Arial',30,'bold') , fill='white')

canvas.grid(column=1,row=1)





window.mainloop()