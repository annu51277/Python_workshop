from tkinter import Canvas, PhotoImage,Tk
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

class TimeBreaks:

    def __init__(self):

        self.count_down_seconds(WORK_MIN)



    def count_down_seconds(self,count):
        count_minutes = math.floor(count / 60)
        count_seconds = count % 60
        window = Tk()
        window.config(bg=YELLOW, padx=100, pady=50)
        canvas = Canvas(bg=YELLOW, highlightthickness=0, width=200, height=224)
        tomato_png = PhotoImage(file='tomato.png')
        canvas.create_image(100, 112, image=tomato_png)
        time = canvas.create_text(100, 130, text='00:00', font=('Arial', 30, 'bold'), fill='white')
        canvas.grid(column=1, row=1)


        if count_seconds == 0:
            count_seconds = '00'
        elif count_seconds < 10:
            count_seconds = f'0{count_seconds}'
        if count_minutes < 10:
            count_minutes = f'0{count_minutes}'
        canvas.itemconfig(time, text=f'{count_minutes}:{count_seconds}')
        if count > 0:
          window.after(1000, self.count_down_seconds, count - 1)  # MS is milli Second

        window.mainloop()