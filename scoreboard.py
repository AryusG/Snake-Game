from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Courier', 24, "bold"))
