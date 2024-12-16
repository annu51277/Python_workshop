from tkinter import Tk, mainloop, Entry, Label, Button , END

window = Tk()
window.title('Covert Miles to Kilo Meters :-)')
window.minsize(width=100,height=50)
window.config(padx=50,pady=25)

label = Label(text='Miles')
label.grid(column=0, row=0 )

result_label = Label(text='', font=('Arial', 10, 'bold'))
result_label.grid(column=0, row=2, columnspan=2)

def convert_miles():
    value = float(entry.get())
    kilo_meters = round(value*1.609,2)
    result_label.config(text=f'is equal to {kilo_meters} Km',font=('Arial',10,'bold'),background='yellow')

def reset():
    entry.delete(0,END)
    result_label.config(text='',background='white')


button = Button(text='Convert to KMs', command=convert_miles)
button.grid(column=1,row=7)

button_reset = Button(text='Reset',command=reset)
button_reset.config(padx=5,pady=5)
button_reset.grid(column=4,row=7)

entry=Entry(width=10,font=('Arial',10,'bold'))
entry.grid(column=1,row=0)


window.mainloop()

