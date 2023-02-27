import turtle

STARTING_COORDINATES = (0, -200)


class Tim(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.left(90)
        self.speed(0)
        self.shape('turtle')
        self.penup()
        self.goto_start()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        if self.ycor() < -270:
            return
        self.backward(10)

    def goto_start(self):
        self.goto(STARTING_COORDINATES)
