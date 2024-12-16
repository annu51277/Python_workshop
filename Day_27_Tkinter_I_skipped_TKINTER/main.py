from tkinter import Tk, Label, Button, Entry , Text , END
from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500,height=300)
my_label = Label(text='I am Label')
my_label.config(padx=50,pady=50)
my_label.grid(column=0,row=0)

def button_click():
    my_label.config(text='Button got clicked ' , background='red')
    my_label.grid(column=0,row=0)

def entry_value():
    value = entry.get()
    my_label.config(text=value, background='yellow')
    my_label.grid(column=0,row=0)
    entry.grid(column=3,row=2)


button_1 = Button(text='Click Me',command=entry_value)
button_1.grid(column=1,row=2)

new_button = Button(text='New_Click Me',command=entry_value)
new_button.grid(column=1,row=3)





entry = Entry(width=10)
print(entry.get())
entry.grid(column=5,row=2)

text = Text(height=5, width=30)
text.focus()
text.grid(column=5,row=4)
text.insert(END, "Example of multi-line text entry.\nHello Mohammad")
print(text.get(0.1,END))



window.mainloop()