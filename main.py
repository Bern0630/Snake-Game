from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=590, height=590)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.snakeHead.distance(food) < 15:
        food.refresh_food_pos()
        scoreboard.count_score()
        snake.extend_snake()

    # detect collision with wall
    if snake.snakeHead.xcor() > 285 or snake.snakeHead.xcor() < -285 or snake.snakeHead.ycor() > 285 or snake.snakeHead.ycor() < -285:
        scoreboard.reset_snake()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.snake[1:]:
        if snake.snakeHead.distance(segment) < 10:
            scoreboard.reset_snake()
            snake.reset_snake()

screen.exitonclick()
