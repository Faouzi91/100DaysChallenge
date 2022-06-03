from turtle import Turtle
from snake import Snake

ALIGN = "center"
FONT = "courier"
FONT_SIZE = 24

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
        self.increase_score()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=(FONT, FONT_SIZE, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN,
                   font=(FONT, FONT_SIZE, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

