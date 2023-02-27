import turtle
import random
turtle.colormode(255)

STARTING_POSITIONS = [-155, -105, -55, -5, 45, 95, 145]


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


class CarManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1, 4)

        if random_chance == 1:
            new_car = turtle.Turtle()
            new_car.penup()
            new_car.right(180)
            new_car.shape('square')
            new_car.color(generate_color())
            new_car.speed(0)
            new_car.goto(x=330, y=random.choice(STARTING_POSITIONS))
            new_car.shapesize(stretch_len=1.5, stretch_wid=1)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if not car.xcor() < -320:
                car.forward(10)

    def increase_speed(self):
        self.car_speed *= 0.5
