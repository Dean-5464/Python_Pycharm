class Animal:


    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def get_animal_species(self):
        return self._species

    def set_animal_name(self, name):
        self.name = name

    def set_animal_species(self, species):
        self.species = species

    def set_animal_age(self, age):
        self.age = age

    def get_animal_age(self):
        return self.age

    def set_animal_sound(self, sound):
        self._sound = sound

    def make_sound(self):
        print(self._sound)


class Cat(Animal):
    _species = "Cat"
    _sound = "Meow"
    _age = "Unknown"

    def __init__(self, name):
        super().__init__(name)


class Dog(Animal):
    _species = "Dog"
    _sound = "Woof"
    _age = "Unknown"

    def __init__(self, name):
        super().__init__(name)

class Bird(Animal):
    _species =  "Bird"
    _sound = "Tweet"
    _age = "Unknown"

    def __init__(self, name):
        super().__init__(name)


def main():

    age = 12

    cat_animal = Cat("Spot")
    dog_animal = Dog("Odi")
    bird_animal = Bird("Tweety")

    bird_animal.set_animal_age(age)
    dog_animal.set_animal_age(age)
    cat_animal.set_animal_age(age)

    animal_list = [cat_animal, dog_animal, bird_animal]

    for animal in animal_list:
        print("The", animal.get_animal_species(), "Goes")
        animal.make_sound()
        print("and is", animal.get_animal_age(), "years old", '\n')


main()
