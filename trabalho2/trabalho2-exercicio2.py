import turtle
from turtle import Turtle, Screen

BG_COLOR = "red"
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
DRAWING_WIDTH = 600
DRAWING_HEIGHT = 600
TITLE = "Tapete de Sierpinski"


def pattern(length, depth):

    if depth < 1:
        return

    turtle.penup()
    turtle.backward(length / 2)
    turtle.left(90)
    turtle.backward(length / 2)
    turtle.right(90)
    turtle.pendown()

    for _ in range(4):
        pattern(length / 2.2, depth - 1)
        turtle.forward(length)
        turtle.left(90)

    turtle.penup()
    turtle.forward(length / 2)
    turtle.left(90)
    turtle.forward(length / 2)
    turtle.right(90)
    turtle.pendown()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)
    
    screen = Screen()
    turtle = Turtle()
    turtle.speed('fastest')

    pattern(300, 4)

    turtle.hideturtle()
    screen.exitonclick()