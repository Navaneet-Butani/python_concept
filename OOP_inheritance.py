class Car:
    # Class attributes
    wheels = 4

    # Initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance method
    def speed(self, dist, time):
        self.dist = dist
        self.time = time
        return "Speed is {} kmph".format(self.dist / self.time)


# Inherit above class
class Sports(Car):
    wheels = 6

    def __init__(self, name, color, weight):
        super().__init__(name, color)           # Initialize parent class
        self.weight = weight


BMW = Car("BMW", "Black")
print(BMW.speed(190, 1.5))
print(BMW.wheels)
print(BMW.name)


Sports_car = Sports("Sports_car", "Red", 300)
print(Sports_car.weight)
print(Sports_car.wheels)

# Method Revolution Order
print(Sports.__mro__)


# Multiple Inheritance
class Bike1:
    wheels = 2

    def display(self):
        print("Bike1")


class Bike2:
    wheels = 3

    def display(self):
        print("Bike2")


class Bike(Bike1, Bike2):
    pass


b1 = Bike1()
b2 = Bike2()
b = Bike()

print(b.wheels)
b.display()
