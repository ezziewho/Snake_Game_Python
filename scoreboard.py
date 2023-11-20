from turtle import Turtle
from food import Food
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')
#high_score_file = open("high_score.txt", mode="w")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"High score: {self.high_score} ", align=ALIGNMENT, font=FONT)
        self.goto(-230, 275)
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            #self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        with open("/Users/48665/OneDrive/Desktop/high_score.txt", mode="r") as highscore_file:
            contents = int(highscore_file.read())
        return contents

    def update_highscore(self):
        with open("../../OneDrive/Desktop/high_score.txt", mode="w") as highscore_file:
            highscore_file.write(str(self.score))
        self.high_score = self.score
