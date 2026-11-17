class Car:
    def __init__(self, model):
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        return f"{self.name} is driving the {car.model}."

my_car = Car("Tesla")
my_driver = Driver("Alice")

print(my_driver.drive(my_car))