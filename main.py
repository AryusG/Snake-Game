from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    snake_part = Turtle('square')
    snake_part.color('white')
    snake_part.penup()
    snake_part.goto(position)











screen.exitonclick()