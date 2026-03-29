import random
from turtle import *
import math

screen = Screen()
screen.bgcolor("white")

hot_palette = [
"hotpink","deeppink","pink",
"#ff69b4","#ff1493","#ff5c8a","#ff4d6d",
"#ff006e","#ff0a54","#ff477e","#ff7096",
"coral","tomato","orangered",
"#ff7b00","#ff8500","#ff9100","#ff9e00",
"#ff5400","#ff6d00","#ff3c38",
"red","crimson",
"#ff1744","#ff1744","#ff355e",
"magenta","fuchsia",
"#ff00ff","#ff00cc","#ff00aa","#ff0099",
"orchid","mediumorchid","darkorchid",
"#d000ff","#c77dff","#9d4edd","#8338ec",
"violet","blueviolet",
"gold","yellow",
"#ffbe0b","#ffd60a","#ffea00",
"#fb5607","#ff006e","#8338ec","#3a86ff"
]

green_palette = ["springgreen","mediumspringgreen","lime","limegreen",
                 "lawngreen","chartreuse","greenyellow","palegreen",
                 "lightgreen","mediumseagreen","seagreen","yellowgreen",
                 "darkseagreen","lightseagreen","#00ff7f","#39ff14",
                 "#7fff00","#66ff66","#99ff66","#66ff99","#33ff99","#00ff99"]



class Flower(Turtle):
    # constructor
    def __init__(self, x :int, y :int, num_petals :int, size :int, petal_colour :str, stamen_colour :str, stem_colour :str):
        super().__init__()
        self.x = x
        self.y = y
        self.num_petals = num_petals
        self.size = size
        self.petal_colour = petal_colour
        self.stamen_colour = stamen_colour
        self.stem_colour = stem_colour

        self.hideturtle()
        self.speed(0)
        self.penup()

    # Draw one petal
    def _draw_one_petal(self, shape :int = 60):
        self.begin_fill()
        self.color(self.petal_colour)
        self.pensize(20)

        for _ in range(2):
            self.circle(self.size, shape)
            self.left(120)

        self.end_fill()
    # Draws all petals
    def _draw_all_petals(self, shape :int = 60):
        for _ in range(self.num_petals):
            self.forward(self.size)
            self.pendown()

            self._draw_one_petal(shape)
            self.penup()
            self.goto(self.x, self.y)
            self.left(360/self.num_petals)
    # Draw stamen
    def _draw_stamen(self):
        self.color(self.stamen_colour)
        self.goto(self.x, self.y - self.size // 5)
        self.dot(self.size)
    # Draw stem
    def _draw_stem(self):
        self.penup()
        self.goto(self.x, self.y - self.size)
        self.color(self.stem_colour)
        self.setheading(270)
        self.pensize(max(1, 15 - self.num_petals))
        self.pendown()
        self.forward(150)
        self.penup()
        print("flower completed")
    # Draw one flower
    def draw_one_flower(self, shape :int = 60):
        self.goto(self.x, self.y)
        self.setheading(270)
        self._draw_all_petals(shape)
        self._draw_stamen()
        self._draw_stem()

# main
for i in range(20):
    f = Flower(
            random.randint(-300, 300),   # random x-coordinate
            random.randint(-300, 300),   # random y-coordinate
            random.randint(6, 12),       # random number of petals
            random.randint(5, 40),       # random flower size
            random.choice(hot_palette),  # random petal color
            random.choice(hot_palette)	,  # random stamen color
            random.choice(green_palette) # random stem color
        )
    f.draw_one_flower(random.randint(30, 180))
# randomisation
mainloop()
