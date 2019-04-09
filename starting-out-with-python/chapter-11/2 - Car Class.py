# A program which creates a Car class, and then creates a couple of functions for
# that object
class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def set_make(self, make):
        self.__make = self
    def set_model_year(self, year_model):
        self.__year_model = year_model
    def accelerate(self, speed):
        self.__speed += 5
    def brake(self, speed):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed

model = 1997
make = 'Toyota'
speed = 0
car = Car(model, make, speed)
for i in range(5):
    car.accelerate(speed)
    print("Here is the car's speed in miles per hour:", car.get_speed())
for i in range(5):
    car.brake(speed)
    print("Here is the car's speed in miles per hour:", car.get_speed())
    
