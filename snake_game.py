import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("coral4")
screen.title("Turtle snake game")
screen.tracer(0)

new_snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.left, "Left")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_snake.move()

 # Food collision detection
    if new_snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        if score.score % 2 == 0:
            new_snake.add_tail()

        if score.score % 10 == 0:
            new_snake.speedup()  # snake speed up

 # Detect collision with wall
    x_cor = new_snake.head.xcor()
    y_cor = new_snake.head.ycor()

    if x_cor > 440 or x_cor < -440 or y_cor > 430 or y_cor < -440:
        game_is_on = False
        score.game_over()

screen.exitonclick()
