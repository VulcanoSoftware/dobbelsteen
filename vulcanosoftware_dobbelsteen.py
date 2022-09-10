import turtle
import random

turtle.speed(0)
turtle.color('white')
turtle.begin_fill()
for n in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.pu()
d=random.randint(1,6)
turtle.color('green')
turtle.goto(30,-80)
turtle.write(d, font=('Arial', 60, 'normal'))
input("")