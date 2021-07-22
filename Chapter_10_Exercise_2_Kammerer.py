class Car:
    __year_model = ""
    __make = ""
    __speed = 0

    def __init__(self, year_model, make):
        __speed = 0
        self.__year_model = year_model
        self.__make = make

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed


def main():

    car = Car("Null", "Null")

    car.accelerate()
    print("Your Current speed is,", car.get_speed())
    car.accelerate()
    print("Your Current speed is,", car.get_speed())
    car.accelerate()
    print("Your Current speed is,", car.get_speed())
    car.accelerate()
    print("Your Current speed is,", car.get_speed())
    car.accelerate()
    print("Your Current speed is,", car.get_speed())

    print()

    car.brake()
    print("Your Current speed is,", car.get_speed())
    car.brake()
    print("Your Current speed is,", car.get_speed())
    car.brake()
    print("Your Current speed is,", car.get_speed())
    car.brake()
    print("Your Current speed is,", car.get_speed())
    car.brake()
    print("Your Current speed is,", car.get_speed())


main()
