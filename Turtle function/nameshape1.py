#https://www.tutorialspoint.com/turtle-graphics-using-python#:~:text=Turtle%20is%20a%20Python%20library%20to%20draw%20graphics.,where%20nice%20graphics%20is%20created.%20Simple%20Turtle%20Commands
# #
from turtle import Turtle, Screen
import time
NAME = "IDAN"

BORDER = 1
BOX_WIDTH, BOX_HEIGHT = 6, 10  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size

def letter_A(turtle):
    turtle.forward(HEIGHT / 2)
    for _ in range(3):
        turtle.forward(HEIGHT / 2)
        turtle.right(90)
        turtle.forward(WIDTH)
        turtle.right(90)
    turtle.forward(HEIGHT)

def letter_D(turtle):
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.circle(-HEIGHT / 2, 180, 30)

def letter_I(turtle):
    turtle.right(90)
    turtle.forward(WIDTH)
    turtle.backward(WIDTH / 2)
    turtle.left(90)
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.backward(WIDTH / 2)
    turtle.forward(WIDTH)

def letter_N(turtle):
    turtle.forward(HEIGHT)
    turtle.goto(turtle.xcor() + WIDTH, BORDER)
    turtle.forward(HEIGHT)

LETTERS = {'A': letter_A, 'D': letter_D, 'I': letter_I, 'N': letter_N}

wn = Screen()
wn.setup(800, 400)  # arbitrary
wn.title("Turtle writing my name: {}".format(NAME))
wn.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = Turtle()

for counter, letter in enumerate(NAME):
    marker.penup()
    marker.goto(counter * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

wn.mainloop()
time.sleep(10)