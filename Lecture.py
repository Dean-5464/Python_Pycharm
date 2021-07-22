class Animal:

    _sound = ""
    _species = "Dog"

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

    def set_animal_sound(self, sound):
        self._sound = sound

    def make_sound(self):
        print(self._sound)


class Cat(Animal):
    _species = "Cat"
    _sound = "Meow"

    def __init__(self, name):
        super().__init__(name)


class Dog(Animal):
    _species = "Dog"
    _sound = "Woof"

    def __init__(self, name):
        super().__init__(name)