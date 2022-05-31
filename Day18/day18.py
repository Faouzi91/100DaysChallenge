import turtle
from turtle import Turtle, Screen
import random
import heroes

tim = Turtle()
tim.color("orangered")
turtle.colormode(255)

screen = Screen()
screen.bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for _ in range(4):
#     new_turtle.forward(100)
#     new_turtle.right(90)

# print(heroes.gen())

# for _ in range (20):
#     new_turtle.pendown()
#     new_turtle.forward(10)
#     new_turtle.penup()
#     new_turtle.forward(10)
angle = [0, 90, 180, 270]
color_list = ["white", "skyblue", "red", "green", "blue", "cyan", "yellow", "magenta", "purple", "red", "orangered"]
tim.pensize(1)
tim.speed("fastest")

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range (num_sides):
#         new_turtle.forward(100)
#         new_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     new_turtle.color(random.choice(color_list))
#     draw_shape(shape_side_n)
tim.color(random_color())

# for _ in range(200):
#     new_turtle.color(random_color())
#     new_turtle.forward(30)
#     new_turtle.setheading(random.choice(angle))






def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)









screen.exitonclick()

