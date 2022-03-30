import time
from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snakeHead = self.snake[0]

    def create_snake(self):
        # snake = []
        # x_pos = [0, -20, -40]
        #
        # for i in range(3):
        #     cute_turtle = Turtle(shape="square")
        #     cute_turtle.color("white")
        #     cute_turtle.penup()
        #     cute_turtle.goto(x=x_pos[i], y=0)
        #     snake.append(cute_turtle)
        # another way to write:
        # start_pos = [(0, 0), (-20, 0), (-40, 0)]
        # for i in start_pos:
        #     cute_turtle = Turtle(shape="square")
        #     cute_turtle.color("white")
        #     cute_turtle.goto(i)

        for pos in START_POS:
            self.increase_segment(pos)

    def increase_segment(self, pos):
        cute_turtle = Turtle("square")
        cute_turtle.color("white")
        cute_turtle.penup()
        cute_turtle.goto(pos)
        self.snake.append(cute_turtle)

    def extend_snake(self):
        self.increase_segment(self.snake[-1].position())

    def reset_snake(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
            time.sleep(0.15)
        self.snake.clear()
        self.create_snake()
        self.snakeHead = self.snake[0]

    def move(self):
        # range(start, stop, step), using len is afraid later will add some more segments
        for snake_num in range(len(self.snake) - 1, 0, -1):
            # get the coordinate xcor & ycor from the front segment
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            # get the coordinate from the front segment and move forward
            self.snake[snake_num].goto(new_x, new_y)
        self.snakeHead.forward(MOVE_DISTANCE)

    def up(self):
        # if snake head is heading downward, it can't go up
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(UP)

    def down(self):
        # if snake head is heading upward, it can't go down
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(DOWN)

    def left(self):
        # if snake head is heading right, it can't go left
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(LEFT)

    def right(self):
        # if snake head is heading left, it can't go right
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(RIGHT)
