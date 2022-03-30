from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.actual_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.actual_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_snake(self):
        if self.actual_score > self.high_score:
            self.high_score = self.actual_score
            with open("data.txt", "w")as data:
                data.write(f"{self.high_score}")
        self.actual_score = 0
        self.update_score()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.actual_score += 1
        self.update_score()
