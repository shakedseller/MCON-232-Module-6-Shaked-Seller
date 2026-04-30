import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

COLLISION = 30

class GameController:
    def __init__(self, snake, food, scoreboard, screen) -> None:
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.screen = screen

    def setup_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def run_game_loop(self):
        print("Game loop")
        is_game_on = True

        self.setup_bindings()
        self.screen.setup(width=700, height=600)
        self.screen.bgcolor("#03045e")
        self.screen.title("Snake")
        self.screen.tracer(0)
        self.screen._root.config(cursor="none")

        self.snake.create_starting_snake()

        while is_game_on:
            time.sleep(0.1)
            self.screen.update()
            self.snake.move()

            self.check_food_collision()
            self.check_wall_collision()
            self.check_self_collision()

    def check_food_collision(self):
        if self.snake.head.distance(self.food) < COLLISION:
            self.snake.grow()
            self.food.refresh()
            self.scoreboard.increase_score()

    def check_wall_collision(self):
        width = turtle.window_width()
        height = turtle.window_height()

        if self.snake.head.xcor() > width / 2 or self.snake.head.xcor() < -width/2 or self.snake.head.ycor() > height / 2 or self.snake.head.ycor() < -height / 2:
            self.reset_round()

    def check_self_collision(self):
        for s in self.snake.segments[3:]:
            if self.snake.head.distance(s) < 15:
                self.reset_round()

    def reset_round(self):
        self.game_over()
        time.sleep(1)
        self.snake.reset()
        self.scoreboard.reset()
        self.food.refresh()

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.color("#d90429")
        self.scoreboard.write(
            f"GAME OVER",
            align="center",
            font=("Arial", 50, "bold")
        )
        self.screen.update()

