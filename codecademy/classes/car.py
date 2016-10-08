class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "like new"


class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)
print(my_car.display_car())
