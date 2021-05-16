from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
screen = Screen()
screen.listen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # TODO Create an attribute
    # TODO Create a method called move

    def __init__(self):
        self.segments = []  # all turtle objects
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle('square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


