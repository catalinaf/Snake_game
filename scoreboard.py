from turtle import Turtle
POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.setposition(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:   {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
