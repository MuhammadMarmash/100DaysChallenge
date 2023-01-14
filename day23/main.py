import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(key="w", fun=player.move_forward)
screen.onkeypress(key="s", fun=player.move_backward)
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.create_car()


def restart():
    car_manager.level = 1
    scoreboard.level = 1
    scoreboard.update_level()
    player.restart_game()
    game()


def game():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        car_manager.create_car()
        for car in car_manager.all_cars:
            car_manager.move(car)
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False
                screen.onkeypress(key="r", fun=restart)

        if player.is_at_finish_line():
            car_manager.level += 1
            scoreboard.increase_level()
            player.restart_game()

        screen.update()

    screen.exitonclick()


game()


