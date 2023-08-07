from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.body = []

    def create(self):
        s = Screen()
        s.tracer(0)
        n = 0
        for _ in range(3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.width(20)
            t.penup()
            t.setx(n)
            n = n-20
            self.body.append(t)
        s.update()

    def extend(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.width(20)
        t.penup()
        t.goto(self.body[-1].position())
        self.body.append(t)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def lose(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()

    def move(self):
        for seg in range(len(self.body)-1, 0, -1):
            new_x = self.body[seg-1].xcor()
            new_y = self.body[seg-1].ycor()
            self.body[seg].goto(new_x, new_y)
        self.body[0].forward(20)






