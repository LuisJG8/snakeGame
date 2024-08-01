from turtle import Turtle
from food import Food

class T_scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move=False, align="center",
                   font=('Arial', 20, 'normal'))

    def write_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="center",
                   font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(arg=f"GAME OVER", move=False, align="center",
                   font=('Arial', 20, 'normal'))