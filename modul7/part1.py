class Car:
    name = "car"
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    # cars_built = []

    def __init__(self, doors=None):
        if doors:
            self.doors = doors
        print('Starting construction')

    def change_car_color(self, color):
        print(f'Changing car {self.name}')
        self.color = color

    def change_car_color_user_input(self):
        print(f'Changing car {self.name}')
        self.color = input('Set new car color:')

    def drive(self, wheels=3):
        print(f"Driving {wheels} wheel drive car")


class Dacia(Car):
    name = "Logan"
    brand = "Dacia"

    def drive(self):
        print("2 wheel drive")


class BMW(Car):
    name = "X3"
    brand = "BMW"

    def drive(self):
        print("4 wheel drive")


car = Car()
car.drive()

dacia = Dacia()
dacia.change_car_color("black")
dacia.drive()

bmw = BMW()
bmw.change_car_color("navy")
bmw.drive()

