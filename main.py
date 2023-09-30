import turtle
import turtledemo.nim

import colorgram
from turtle import *
from random import *

turtle.colormode(255)
colors = colorgram.extract('image.jpg', 30)
colors_rgb = []


for color in colors:
    # colors_rgb.append(first_color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_rgb.append((r, g, b))
# print(colors_rgb)

y_direction = -300
tom = Turtle()
tom.speed("fastest")
tom.penup()
tom.goto(-325, y_direction)
tom.pendown()
tom.speed("fast")

count = 0
for _ in range(200):
    tom.dot(20, choice(colors_rgb))
    tom.penup()
    tom.forward(50)
    count += 1
    if count % 14 == 0:
        tom.penup()
        y_direction += 50
        tom.goto(-325, y_direction)
        tom.pendown()


screen = Screen()
screen.exitonclick()