BACKGROUND_COLOR = "#B1DDC6"

from tkinter import Tk, PhotoImage, Canvas, Button, messagebox
import pandas as pd
import random
from pandas.errors import EmptyDataError



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Flash Cards')
window.config(padx=100, pady=100, background=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526)
canvas.grid(column=1, row=0)
french_image = PhotoImage(file='card_front.png')
english_image = PhotoImage(file='card_back.png')
canvas_image = canvas.create_image(410, 263, image=french_image)
initial_image = canvas.create_text(400, 150, text="", fill="black", font=('Arial', 40, 'italic'))

# Create a placeholder for the French and English word
french_word_display = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))

# ---------------------------- Word Display Mechanism ------------------------------- #
# Read the CSV into a DataFrame

to_learn = {}
current_card = {}
original_data = {}

try:
    df = pd.read_csv('learn/words_to_learn.csv')

except EmptyDataError:
    messagebox.showinfo(title='Congratulations', message=f'Completed all words')
    df = pd.read_csv('learn/french_words.csv')
    original_data = df.to_dict(orient='records')
    to_learn = original_data

except FileNotFoundError:
    df = pd.read_csv('learn/french_words.csv')
    original_data = df.to_dict(orient='records')
    to_learn = original_data

else:
    to_learn = df.to_dict(orient='records')



def reset_cards():
    global to_learn
    canvas.itemconfig(canvas_image, image=french_image)
    reset_data = pd.read_csv('learn/french_words.csv')
    new_reset_data = reset_data.to_dict(orient='records')
    to_learn = new_reset_data
    print(len(to_learn))
    show_next_word()

def show_next_word():
    try:
        global current_card
        current_card = random.choice(to_learn)
        canvas.itemconfig(initial_image, text='French')
        canvas.itemconfig(french_word_display, text=current_card['French'])  # Update the canvas text
        # Schedule the next word to be shown in 3 seconds
        window.after(3000, show_english_word)
    except IndexError:
        messagebox.showinfo(title='Congratulations', message=f'Completed all words')

def show_english_word():
    canvas.itemconfig(initial_image, text='English',fill='black',font=('Arial', 40, 'bold'))
    canvas.itemconfig(canvas_image, image=english_image)
    canvas.itemconfig(french_word_display, text=current_card['English'],fill='purple')

   # else:
   #      messagebox.showinfo(title='Info', message='No more records')
   #      reset_flashcards()

def next_word_on_button_click():
    canvas.itemconfig(canvas_image, image=french_image)
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv('learn/words_to_learn.csv', index=False)
    show_next_word()

def cross_button():
    canvas.itemconfig(canvas_image, image=french_image)
    show_next_word()
    # revisit_cards = current_card
    # data = pd.DataFrame(to_learn)
    # data.to_csv('learn/words_to_learn.csv',index=False)




# ---------------------------- Button Setup ------------------------------- #

button_right_image = PhotoImage(file='right.png')
button_right = Button(image=button_right_image, highlightthickness=0, command=next_word_on_button_click)
button_right.config(padx=50)
button_right.grid(column=2, row=1)

button_left_image = PhotoImage(file='wrong.png')
button_left = Button(image=button_left_image, highlightthickness=0, command=cross_button)
button_left.config(padx=50)
button_left.grid(column=0, row=1)

button_reset = Button(text='RESET', highlightthickness=0, command=reset_cards)
button_reset.config(padx=50)
button_reset.grid(column=1, row=1)

# Start the word display mechanism
show_next_word()  # Start showing the words after the UI loads

window.mainloop()
