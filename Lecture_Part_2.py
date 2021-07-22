from Lecture import Animal, Cat, Dog


def main():

    cat_animal = Cat("Spot")
    dog_animal = Dog("Odi")

    animal_list = [cat_animal, dog_animal]

    for animal in animal_list:
        print("The", animal.get_animal_species(), "Goes")
        animal.make_sound()


main()
