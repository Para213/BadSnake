from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scor = 0  #puncte
        self.color("white")
        self.penup()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read(), base=10)
        self.hideturtle()
        self.goto(0,280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"scor: {self.scor} High Score: {self.high_score}", False, align="center", font=(25))

    def reset(self):
        if self.scor > self.high_score:
            self.high_score = self.scor
            with open("data.txt", mode="w") as file:
                file.write(str(self.scor))
        self.scor = 0
        self.update()

    def increase_score(self):
        self.scor += 1
        self.update()