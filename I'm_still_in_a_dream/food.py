from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("#80ed99")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.refresh()

    def random_position(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)

        return (x, y)
    def refresh(self):
        self.goto(self.random_position())

