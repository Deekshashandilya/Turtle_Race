import random
from turtle import *

screen = Screen()

is_Flag = False

screen.setup(width=600, height=500)
user_input = screen.textinput(title="Let's Make a bet !!", prompt="What you think which Turtle will WIN ?")
color_list = ["orange", "red", "yellow", "green", "blue", "purple"]

x_pos = -280
y_pos = -100

turtle_list = []
for colorname in color_list:
    name = Turtle(shape='turtle')
    name.color(colorname)
    name.penup()
    name.goto(x=x_pos, y=y_pos)
    y_pos += 50
    turtle_list.append(name)

if user_input:
    is_Flag = True

while is_Flag:
    for turtle_x in turtle_list:
        if turtle_x.xcor() > 280:
            winning_color = turtle_x.pencolor()
            is_Flag=False

            if winning_color == user_input:
                print(f"You have won !!")
            else:
                print(f"You have lost !!{winning_color} ")
        rand_num = random.randint(0, 10)
        turtle_x.forward(rand_num)

screen.exitonclick()



