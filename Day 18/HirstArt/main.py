# this code gets an image and makes a color pallet form it.
# it's commented out because you only need to do it once because it will be the same each time so you can just copy and paste the outcome
#
# import colorgram
#
# test = colorgram.extract("dhs3823_0_1280_0-1024x958.jpg",34)
# # print(test)
# rgblist = []
# for i in test:
#     r = i.rgb.r
#     b = i.rgb.b
#     g = i.rgb.g
#     test = (r,g,b)
#     rgblist.append(test)
#     # print(rgblist)
# print(rgblist)

rgblist = [(235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]

##########################################################

import turtle
from turtle import Turtle,Screen
from random import choice

t = Turtle()
t.speed(0)
turtle.colormode(255)
turtle.screensize(4000,4000)
t.pencolor("white")

def draw():
    t.fillcolor(choice(rgblist))
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.forward(50)

for i in range(5):
    for i in range(10):
        draw()
    t.setheading(90)
    t.forward(100)
    t.setheading(180)
    t.forward(50)
    for i in range(10):
        draw()
    t.setheading(90)
    t.forward(20)
    t.setheading(0)
    t.forward(50)

screen = Screen()
screen.exitonclick()
