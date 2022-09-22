from turtle import Turtle
POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


def get_high_score():
    with open("data.txt") as file:
        latest_high_score = int(file.read())
    return latest_high_score


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.hideturtle()
        self.up()
        self.setposition(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}   High score:  {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.store_high_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def store_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
