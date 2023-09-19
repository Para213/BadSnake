from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scor = 0  #puncte
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"scor: {self.scor}", False, align="center")

    def update(self):
        self.scor += 1
        self.clear()
        self.write(f"scor: {self.scor}", False, align="center")

    def finalScore(self):
        self.clear()
        self.home()
        self.write(f"Scor Final: {self.scor}", False, align="center", font=('Arial', 50))