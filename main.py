from turtle import *

def main():
    """
    Initialize the flower class with describe and grow as member functions
    """
    class Flower:
        def __init__(self, name :str, petals :int, color :str, height :int):
            self.name = name
            self.petals = petals
            self.color = color
            self.height = height

        def describe(self):
            return f"{self.name} is {self.color}, has {self.petals} petals, and is {self.height}cm tall."

        def grow(self, cm :int = 1):
            self.height += cm


    # Thank you to my sister for giving me these flower species

    """
    Initializing four flower objects
    """
    plum_blossom = Flower("Plum Blossom", 5, "light pink", 40)
    petunia = Flower("Petunia", 5, "magenta", 15)
    windflower = Flower("Windflower", 10, "white", 10)
    cosmos = Flower("Cosmos", 8, "vibrant pink", 30)

    """
    Storing all the flower objects in a list
    """
    garden = [plum_blossom, petunia, windflower, cosmos]

    """
    Print the flower information before and after it's updated
    """
    print("----FLOWER INFO----\n")
    for f in garden:
        print(f.describe())
        f.grow()

    print("\n----AFTER UPDATING----\n")
    for f in garden:
        print(f.describe())

    """
    Draws the flowers using turtle graphics
    """
    class Draw_Flower(Turtle):
        pass

        # constructor
        def __init__(self, x: int, y: int, num_petals: int, size: int, petal_colour: str, stamen_colour: str,
                     stem_colour: str):
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
        def _draw_one_petal(self, shape: int = 60):
            self.begin_fill()
            self.color(self.petal_colour)
            self.pensize(20)

            for _ in range(2):
                self.circle(self.size, shape)
                self.left(120)

        def _draw_all_petals(self, shape: int = 60):
            for _ in range(self.num_petals):
                self.forward(self.size)
                self.pendown()

                self._draw_one_petal(shape)
                self.penup()
                self.goto(self.x, self.y)
                self.left(360 / self.num_petals)

        def _draw_stamen(self):
            self.color(self.stamen_colour)
            self.goto(self.x, self.y - self.size // 5)
            self.dot(self.size)

        def _draw_stem(self):
            self.penup()
            self.goto(self.x, self.y - self.size)
            self.color(self.stem_colour)
            self.setheading(270)
            self.pensize(max(1, 15 - self.num_petals))
            self.pendown()
            self.forward(150)
            self.penup()

        def draw_one_flower(self, shape: int = 60):
            self.goto(self.x, self.y)
            self.setheading(270)
            self._draw_all_petals(shape)
            self._draw_stamen()
            self._draw_stem()

    """
    Create a Draw_Flower object for each flower
    """
    d_plum_blossom = Draw_Flower(
        -300,
        0,
        plum_blossom.petals,
        plum_blossom.height,
        "#FAD2E1",
        "#FFF1E6",
        "#99D98C"
    )

    d_petunia = Draw_Flower(
        -200,
        0,
        petunia.petals,
        petunia.height,
        "#D91159",
        "#FBB13C",
        "#218380"
    )

    d_windflower = Draw_Flower(
        -100,
        0,
        windflower.petals,
        windflower.height,
        "#EFEBCE",
        "#D6CE93",
        "#A3A380"
    )

    d_cosmos = Draw_Flower(
        0,
        0,
        cosmos.petals,
        cosmos.height,
        "#F283B6",
        "#EDBFB7",
        "#6E9887"
    )

    """
    Draws each flower
    """
    d_plum_blossom.draw_one_flower()
    d_petunia.draw_one_flower()
    d_windflower.draw_one_flower()
    d_cosmos.draw_one_flower()

    """
    Keeps the turtle window open
    """
    mainloop()

main()