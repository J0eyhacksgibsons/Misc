from tabnanny import check
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",20,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 270)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.check_high_score()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",  align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        """Checks high score from the data.txt file"""
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.check_high_score()
        self.update_scoreboard()
    
    def one_more_point(self):
        self.score += 1
        self.update_scoreboard()