from turtle import Screen
from snakeB import Snake
from food import Food
from scoreboard import T_scoreboard
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

rand_x = random.randint(-280, 280)
rand_y = random.randint(-280, 280)

snake = Snake()
food = Food()
scoreboard = T_scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.write_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[:1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()