# Elijah Budd
# 4/1/2025
# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.
# These values should be assigned to the object's __year_model and __make data attributes.
# It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it is called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelerate method, get the current speed of the car and display it.
# Then call the brake method.
# After each call to the brake method, get the current speed of the car and display it.

class Car:
    def __init__(self, year_model, make):
        self.year = year_model
        self.make = make

        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

if __name__ == '__main__':
    def car():
        my_car = Car(2024, 'Toyota')

        for x in range(5):
            my_car.accelerate()
            print("The current speed is: ", my_car.get_speed(), "mph")

        my_car.brake()
        print("The current speed is: ", my_car.get_speed(), "mph")

    car()
