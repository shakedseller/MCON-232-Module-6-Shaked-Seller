from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#90e0ef")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.goto(0, 260)
        self.color("#90e0ef")
        self.score = 0
        self.update_scoreboard()