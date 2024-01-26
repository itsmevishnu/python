import turtle
from turtle import *

#create screen
screen =  turtle.Screen()
# create turtle instance
t = turtle.Turtle()
turtle.speed(0)
start_x = -300
start_y = 250
width = 450
height = width*2/9
offset = height*0.1
radius = (height/2)-offset
inner_radius = radius-5

t.penup()
t.color('navy')
t.goto(start_x/2, start_y+10)
style = ('Comic Sans MS', 30, 'bold')
t.pendown()
t.write('Happy Republic Day!!!', font=style, move=False, align='center')
#set pen to intial 
t.penup()
t.goto(start_x,start_y)
t.pendown()

#orange box
t.color("orange")
t.begin_fill()
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.end_fill()
t.penup()

#green box
t.goto(start_x, start_y-(2*height))
t.pendown()
t.color("green")
t.begin_fill()
t.right(180)
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.end_fill()

#circle blue
t.penup()
t.goto(start_x+(width/2),start_y-height-offset)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(radius)
t.end_fill()

#cicle white

t.penup()
t.goto(start_x+(width/2),start_y-(height)-offset-5)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(inner_radius)
t.end_fill()

#Points
t.penup()
t.goto(start_x+(width/2)-5,start_y-height-offset-7)
t.pendown()
t.right(180)
t.color("red")
t.begin_fill()
for i in range(24):
    t.color("navy")
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(2*3.14*inner_radius/24)
    t.right(15)
    t.pendown

# spokes
t.penup()
t.goto(start_x+(width/2),start_y-(3*height/2))
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(radius)
    t.backward(radius)
    t.left(15)

#Exits on click
screen.exitonclick()