import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
is_race_on = False
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        turtle.forward(random.randint(0, 10))



# def move_forwards():
#     new_turtle.forward(10)
#
# def move_backward():
#     new_turtle.backward(10)
#
# def turn_left():
#     new_heading = new_turtle.heading() + 10
#     new_turtle.setheading(new_heading)
#
# def turn_right():
#     new_heading = new_turtle.heading() - 10
#     new_turtle.setheading(new_heading)
#
# def clear():
#     new_turtle.clear()
#     new_turtle.reset()
#
# screen.listen()
# screen.onkey(key="d", fun=move_forwards)
# screen.onkey(key="q", fun=move_backward)
# screen.onkey(key="z", fun=turn_left)
# screen.onkey(key="s", fun=turn_right)
# screen.onkey(key="c", fun=clear)


screen.exitonclick()
