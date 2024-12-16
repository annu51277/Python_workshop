from random import shuffle
from sys import api_version
from tkinter import Canvas, Tk, PhotoImage , Label , Entry , END , Button , messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','10']
    symbol = ['!','@','#','$','?','~']


    alphabets = [random.choice(letters) for _ in range( random.randint(1,8))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    spcial_char = [random.choice(symbol) for _ in range(random.randint(2,4))]

    password = alphabets + password_numbers + spcial_char
    shuffle(password)
    joined_list = ''.join(password)
    entry_password.insert(0,joined_list)
    pyperclip.copy(joined_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def website():
    value_website = entry_website.get()
    value_email = entry_email.get()
    value_password = entry_password.get()


    if len(value_website) == 0:
        messagebox.showinfo(title='Oops', message=f'website cannot  be NULL')

    elif  len(value_email)  == 0:
        messagebox.showinfo(title='Oops', message=f'Email cannot  be NULL')

    elif len(value_password)  == 0:
        messagebox.showinfo(title='Oops', message= f'Password cannot  be NULL')

    else:
        is_ok = messagebox.askokcancel(title='Data',message=f'These are details you entered{value_website}, {value_email},{value_password}')

        if is_ok:



            with open(file='data.txt',mode='a') as data:
                data.write(f'{value_website}    |   {value_email}  |   {value_password}\n')
            entry_website.delete(0,END)
            entry_password.delete(0,END)
        else:
            entry_website.delete(0, END)
            entry_password.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50 ,pady=50)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)


label = Label(text="Website:",font=('Arial',10))
label.grid(column=0,row=1)
label_email = Label(text='Email/Username:',font=('Arial',10))
label_email.grid(column=0,row=2)

label_password = Label(text='Password:',font=('Arial',10))
label_password.grid(column=0,row=3)



entry_website = Entry(width=35)
entry_website.focus()
# Puts cursor in the text box
entry_website.grid(column=1,row=1,columnspan=2)

entry_email = Entry(width=35)
entry_email.insert(END,string='ansarrahamath@gmail.com')
entry_email.grid(column=1,row=2,columnspan=2)


entry_password = Entry(width=21)
entry_password.grid(column=1,row=3,columnspan=1)


button = Button(text="Generate Password",command=generator)
button.grid(column=3,row=3)

button_add = Button(text="ADD",width=35,command=website)
button_add.grid(column=1,row=4,columnspan=2)

window.mainloop()