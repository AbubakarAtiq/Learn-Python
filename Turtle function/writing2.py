#import package
import turtle
import time
#write text
#styling font
turtle.write("Happy Birthday Deborah Eric",font=("verdana",15,"normal"))
time.sleep(5)
from turtle import Turtle, Screen
from tkinter.font import Font

TEXT = "Happy Birthday Deborah Eric"  # arbitrary text
POSITION = (150, 150)  # arbitrary position

FONT_SIZE = 36  # arbitrary font size
FONT = ('Arial', FONT_SIZE, 'normal')  # arbitrary font

X, Y = 0, 1

def box(turtle, lower_left, upper_right):
    """ Draw a box but clean up after ourselves """

    position = turtle.position()
    isdown = turtle.isdown()

    if isdown:
        turtle.penup()

    turtle.goto(lower_left)
    turtle.pendown()
    turtle.goto(upper_right[X], lower_left[Y])
    turtle.goto(upper_right)
    turtle.goto(lower_left[X], upper_right[Y])
    turtle.goto(lower_left)

    turtle.penup()
    turtle.setposition(position)

    if isdown:
        turtle.pendown()

screen = Screen()

marker = Turtle(visible=False)
marker.penup()
marker.goto(POSITION)

start = marker.position()
marker.write(TEXT, align='center', move=True, font=FONT)
end = marker.position()

font_config = Font(font=FONT)
font_ascent = font_config.metrics('ascent')
buffer = (font_config.metrics('linespace') - font_ascent) / 2

# Since it's centered, the end[X] - start[X] represents 1/2 the width
box(marker, (2 * start[X] - end[X], start[Y] - buffer), (end[X], start[Y] + font_ascent + buffer))

screen.exitonclick()