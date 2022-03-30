from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh_food_pos()

    def refresh_food_pos(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
