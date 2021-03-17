import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.mov_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        player.reset_pos()
        car.inc_speed()
        scoreboard.update_level()

screen.exitonclick()