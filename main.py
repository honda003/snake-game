from turtle import Screen
from food import Food
import time
from snake import Snake
from score_board import ScoreBoard
s = Screen()
s.bgcolor("black")
s.title("Snake Game")
s.setup(600, 600)
x = Snake()
x.create()
f = Food()
y = ScoreBoard()
s.listen()
s.onkey(x.up, "Up")
s.onkey(x.down, "Down")
s.onkey(x.left, "Left")
s.onkey(x.right, "Right")
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    x.move()
    if x.body[0].distance(f) < 15:
        f.refresh()
        y.increase_score()
        x.extend()

    if x.body[0].xcor() > 290 or x.body[0].xcor() < -290 or x.body[0].ycor() > 290 or x.body[0].ycor() < -290:
        y.reset()
        x.lose()
        x.create()

    for bodies in x.body[1:]:
        if x.body[0].distance(bodies) < 10:
            y.reset()
            x.lose()
            x.create()


s.exitonclick()



