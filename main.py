from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()








screen.exitonclick()