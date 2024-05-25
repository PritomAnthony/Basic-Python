from turtle import Turtle, Screen
new_turtle = Turtle()
new_turtle.shape("turtle")
new_screen = Screen()
new_screen.bgcolor("sandybrown")



def forward():
    new_turtle.forward(10)


def backward():
    new_turtle.back(10)


def right():
    new_turtle.right(20)


def left():
    new_turtle.left(20)


new_screen.listen()
new_screen.onkeypress(forward, "Up")
new_screen.onkeypress(backward, "Down")
new_screen.onkeypress(right, "Right")
new_screen.onkeypress(left, "Left")
new_screen.exitonclick()
