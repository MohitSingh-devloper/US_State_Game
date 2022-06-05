import pandas
import turtle

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
#
#
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Guessed:", prompt="What's another state name?").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("State_Missed.csv")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
