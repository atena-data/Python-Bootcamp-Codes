from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def set_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randrange(-250, 250, 30)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
