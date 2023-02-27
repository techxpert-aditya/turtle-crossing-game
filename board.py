import turtle

LANES = [-130, -80, -30, 20, 70, 129]


class Board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.draw_starting_line()
        self.draw_finish_line()
        self.draw_lanes()

    def draw_starting_line(self):
        self.penup()
        self.goto(-320, -170)
        self.pendown()
        self.forward(640)

    def draw_finish_line(self):
        self.penup()
        self.goto(-320, 170)
        self.pendown()
        self.forward(640)

    def draw_lanes(self):
        for lane in LANES:
            self.penup()
            self.goto(-300, lane)
            while self.xcor() < 300:
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)
