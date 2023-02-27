import turtle
BOARD_COORDINATES = (0, 270)
FONT = ('arial', 16, 'normal')
ALIGN = 'center'


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.score = 0
        self.goto(BOARD_COORDINATES)
        self.show_score()

    def show_score(self):
        self.write(f'score = {self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over.', align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
