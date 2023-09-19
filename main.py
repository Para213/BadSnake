from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Create and config screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #stops animatios

#initializare sarpe, mancare, scor
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#controale
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.update()
        snake.feedSnake()
        print("niam")

    #Detect collision with outside
    if (snake.head.pos() > (300, 0) or snake.head.pos() < (-300, 0) or snake.head.ycor() > 300 or snake.head.ycor() < -300):
        game_is_on = False


    for segment in snake.segments:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            game_is_on = False

snake.endSnake()
scoreboard.finalScore()
time.sleep(5)