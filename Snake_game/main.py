from turtle import Turtle, Screen
from gamecontroller import GameController
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake_game = GameController(snake, food, scoreboard, screen)
snake_game.run_game_loop()

screen.exitonclick()