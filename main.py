import turtle
import tim
import time
import score_board
import board
import car_manager

screen = turtle.Screen()
screen.title('turtle crossing game')
screen.setup(width=600, height=600)

tim = tim.Tim()
score_board = score_board.ScoreBoard()
board = board.Board()
car_manager = car_manager.CarManager()

game_is_on = True
screen.listen()
screen.tracer(0)


while game_is_on:
    time.sleep(car_manager.car_speed)

    # move the cars
    car_manager.create_car()
    car_manager.move()

    # listening to the key press
    screen.onkeypress(fun=tim.move_up, key='Up')
    screen.onkeypress(fun=tim.move_down, key='Down')
    screen.update()

    # updating the score
    if tim.ycor() >= 200:
        score_board.update_score()
        tim.goto_start()
        car_manager.increase_speed()

    # detecting collision
    for car in car_manager.all_cars:
        if tim.distance(car) < 25 and car.xcor() != 0:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
