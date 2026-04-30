from turtle import Screen, Turtle

class Snake():
    def __init__(self) -> None:
        #super().__init__()
        self.segments = []
        self.head = []

    def create_starting_snake(self):
        for i in range(3):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            if i == 0:
                segment.color("#90e0ef")
            else:
                segment.color("#00b4d8")
            segment.goto(20 * i, 0)
            self.segments.append(segment)
        self.head = self.segments[0]

    def move(self):
        for s in range(len(self.segments) -1, 0, -1):
            x = self.segments[s - 1].xcor()
            y = self.segments[s - 1].ycor()
            self.segments[s].goto(x, y)

        self.head.forward(20)

    def grow(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()

        new = Turtle()
        new.penup()
        new.shape("square")
        new.color("#00b4d8")
        new.goto(x, y)

        self.segments.append(new)

    def reset(self):
        for s in self.segments:
            s.hideturtle()
        self.segments.clear()
        self.create_starting_snake()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
