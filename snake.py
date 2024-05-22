from turtle import Turtle
START_POS = [(0, 0), (-5, 0), (-10, 0), (-15, 0), (-20, 0), (-25, 0)]



class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        self.speed = 10

    def create_snake(self):
        for i in START_POS:
            body = Turtle("circle")
            body.color("white")
            body.penup()
            body.goto(i)
            self.parts.append(body)

    def add_tail(self):
        x_cor = self.parts[-1].xcor()
        y_cor = self.parts[-1].ycor()
        if x_cor >= 400 or x_cor <= -400 or y_cor >= 400 or y_cor <= -400:
            return

        body = Turtle("circle")
        body.color("white")
        body.penup()
        body.goto(x_cor - 20, y_cor)
        self.parts.append(body)

    def move(self):
        for parts_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[parts_num - 1].xcor()
            new_y = self.parts[parts_num - 1].ycor()
            self.parts[parts_num].goto(new_x, new_y)
        self.head.forward(self.speed)


    def speedup(self):
        self.speed += 4

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.move()
        else:
            return

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move()
        else:
            return


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move()
        else:
            return

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move()
        else:
            return
