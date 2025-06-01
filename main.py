from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.tracer(0)

w = Turtle()
w.penup()
w.goto(-280, 250)
w.pencolor('black')
w.hideturtle()

screen.title("U.S. States Game")
screen.setup(700,600)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

count = 0
data = pandas.read_csv('50_states.csv')
data.to_csv('learning_states.csv',index=False)
data_learn = pandas.read_csv('learning_states.csv')
screen.update()

def add_state(answer,x,y):
    t = Turtle()
    t.penup()
    t.goto(x,y)
    t.pencolor('black')
    t.hideturtle()
    t.write(f"{answer}",align="center", font=("Arial", 6, "bold"))

def score(u_count):
    w.clear()
    w.write(f"Score: {u_count}/50",align="left", font=("Arial", 18, "bold"))


while count < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's the state name?").title()
    screen.update()

    if answer_state in data.state.values and answer_state in data_learn.state.values:
        count += 1
        score(count)
        add_state(answer_state,data.x[data.state == answer_state].iloc[0],data.y[data.state == answer_state].iloc[0])
        data_learn = data_learn[data_learn.state != answer_state]
        data_learn.to_csv('learning_states.csv', index=False)
        screen.update()

    elif answer_state == 'Exit':
        print(f"Missing states: \n {data_learn.state}")
        screen.bye()
        break

    else:
        answer_state = screen.textinput(title="Wrong! Try Again", prompt="What's the state name?").title()
        screen.update()

