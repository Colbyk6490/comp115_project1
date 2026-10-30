# elden ring drawing
import turtle
import random
wn=turtle.Screen()
wn.setup(width=1.0, height=1.0)
pen=turtle.Turtle()
wn.bgcolor("black")
pen.speed(15)
pen.shape("turtle")
def stars():
    pen.color("white")
    for i in range(100):
        rand1=random.randrange(-750,751)
        rand2=random.randrange(-200,500)
        pen.up()
        pen.goto(rand1,rand2)
        pen.down()
        pen.begin_fill()
        pen.circle(3)
        pen.end_fill()
    return stars
stars()
pen.speed(10)
def horizon():  
    pen.color("darkgreen")
    pen.up()
    pen.goto(0,-200)
    pen.down()
    pen.begin_fill()
    pen.right(10)
    pen.forward(1000)
    pen.up()
    pen.goto(0,-200)
    pen.left(200)
    pen.down()
    pen.forward(1000)
    pen.setheading(270)
    pen.forward(100)
    pen.setheading(0)
    pen.forward(2000)
    pen.setheading(90)
    pen.forward(100)
    pen.end_fill()
    return horizon
horizon()
pen.width(20)

def castle():
    pen.up()
    pen.width(10)
    pen.color("grey")
    pen.goto(-700,-50)
    pen.down()
    pen.setheading(-90)
    pen.begin_fill()
    pen.forward(275)
    pen.left(100)
    pen.forward(525)
    pen.setheading(90)
    pen.forward(225)
    pen.setheading(200)
    pen.circle(-1000,30)
    pen.end_fill()
    pen.begin_fill()
    pen.fillcolor("dimgrey")
    for i in range(2):
        pen.circle(-10,180)
        pen.left(30)
        pen.circle(-1000,30)
    pen.end_fill()
    return castle
castle()
pen.width(20)

def person_head():
    pen.setheading(0)
    pen.color("grey")
    pen.up()
    pen.goto(10,-210)
    pen.down()
    pen.begin_fill()
    pen.circle(-20)
    pen.end_fill()
    pen.up()
    pen.goto(10,-225)
    pen.down()
    pen.setheading(225)
    pen.forward(100)
    return person_head
person_head()

def person_legs():
    angle=-80
    for colour in ["dimgrey","grey"]:
        pen.up()
        pen.goto(-62,-300)
        pen.down()
        pen.setheading(angle)
        angle=angle-20
        pen.color(colour)
        pen.forward(70)
        pen.setheading(180)
        pen.forward(70)
    return person_legs
person_legs()

def sword():
    pen.width(3)
    pen.up()
    pen.color("black")
    pen.goto(50,-250)
    pen.down()
    pen.setheading(-90)
    pen.begin_fill()
    for i in range(2):
        pen.forward(150)
        pen.left(90)
        pen.forward(5)
        pen.left(90)
    pen.end_fill()
    pen.up()
    pen.goto(50,-400)
    pen.setheading(-45)
    pen.down()
    for i in range(4):
        pen.forward(3.5)
        pen.left(90)
    pen.up()
    pen.goto(30,-310)
    pen.down()
    pen.setheading(25)
    pen.forward(50)
    return sword
sword()


def person_arms():
    pen.width(20)
    angle=-75
    for colour in ["dimgrey","grey"]:
        pen.up()
        pen.color(colour)
        pen.goto(-10,-250)
        pen.setheading(angle)
        pen.down()
        pen.forward(50)
        pen.left(90)
        pen.forward(50)
        angle=angle+10

    return person_arms
person_arms()

def elden_ring ():
    pen.width(3)
    pen.up()
    pen.goto(0,0)
    pen.setheading(0)
    pen.down()
    for i in [(66,0),(-66,0),(0,100)]:
        pen.color("yellow")
        pen.up()
        pen.goto(i)
        pen.down()
        pen.circle(100)
    pen.up()
    pen.goto(0,-25)
    pen.setheading(90)
    pen.down()
    pen.forward(425)
    pen.right(90)
    pen.circle(1000,10)
    pen.up()
    pen.goto(0,400)
    pen.setheading(180)
    pen.down()
    pen.circle(-1000,10)
    return elden_ring
elden_ring()

def title():
    pen.color("gold")
    pen.up()
    pen.setheading(-90)
    pen.goto(-325,300)
    pen.write("ELDEN RING",font=("Garamond",75,"bold"))
    return title
title()
pen.hideturtle()
wn.exitonclick()
