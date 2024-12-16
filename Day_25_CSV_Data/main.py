import turtle as t

import pandas as pd


screen_us = t.Screen()

screen_us.title('U.S. States Game')
image = 'blank_states_img.gif'
screen_us.addshape(image)
t.shape(image)

def get_mouse_click_coor(x,y): # This is used to capture the click locations
    print(x,y)


data = pd.read_csv('50_states.csv')

guessed_states = []
is_game_on = True
attempts = 3
while len(guessed_states) < 50:
    guess = screen_us.textinput(f'{len(guessed_states)} of 50: guessed', 'State Name ?').lower()
    for st in data['state']:
        if st.lower() == guess:
            s = data[data['state'] == st ]
            xcor = s['x'].item()
            ycor = s['y'].item()
            tom = t.Turtle()
            tom.hideturtle()
            tom.color('black')
            tom.penup()
            tom.goto(xcor,ycor)
            tom.write(st)
            guessed_states.append(st)



screen_us.listen()
screen_us.onscreenclick(get_mouse_click_coor)
t.mainloop()



screen_us.exitonclick()