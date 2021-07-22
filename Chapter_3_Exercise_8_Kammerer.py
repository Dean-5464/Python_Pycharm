# Chapter 3
# Exercise 8
# Dean Kammerer


def main():

    guests_number = int(input("Please input the number of guests attending >> "))
    hot_dog_number = int(input("Please input the number of hot dogs given to each guest >> "))

    minimum_packages = int((guests_number*hot_dog_number) / 10)
    minimum_buns = int((guests_number*hot_dog_number) / 8)

    remaining_hot_dogs = int((guests_number*hot_dog_number) % 10)
    remaining_buns = int((guests_number*hot_dog_number) % 8)

    print("The minimum amount of hot dog packages needed is", minimum_packages)
    print("The minimum amount of bun packages needed is", minimum_buns)
    print("The remaining amount of hot dogs is", remaining_hot_dogs)
    print("The remaining amount of buns is", remaining_buns)


main()
