from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.current_score} Highest score: {self.high_score}", False, "center", ("Arial", 20, "normal"))

    def increase_score(self):
        self.clear()
        self.hideturtle()
        self.current_score = self.current_score + 1
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.write(f"Score: {self.current_score} Highest score: {self.high_score}", False, "center",("Arial", 20, "normal"))

    def reset(self):
        self.clear()
        self.current_score = 0
        self.write(f"Score: {self.current_score} Highest score: {self.high_score}", False, "center", ("Arial", 20, "normal"))
        with open("data.txt",mode="w") as file:
            content = file.write(f"{self.high_score}\n")
            print(content)





    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", False, "center", ("Arial", 20, "normal"))








