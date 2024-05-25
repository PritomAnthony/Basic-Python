import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-430, 430)
        rand_y = random.randint(-430, 420)
        self.goto(rand_x, rand_y)