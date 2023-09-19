from turtle import Turtle


STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for pos in STARTING_POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.setx(pos)
            self.segments.append(new_turtle)

    def feedSnake(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].pos())
        self.segments.append(new_turtle)

    def endSnake(self):
        for segment in self.segments:
            segment.hideturtle()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)