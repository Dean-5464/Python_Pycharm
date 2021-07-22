import random


def generated_number():

    number = random.randint(1, 100)

    return number


def main():
    odd_counter = 0
    even_counter = 0

    for cycle in range(1, 101):

        generated_number()

        if generated_number() % 2 != 0:
            odd_counter = odd_counter + 1
        else:
            even_counter = even_counter + 1

    print("The Number of Even Values Are:", even_counter, "And The Number of Odd Values Are:", odd_counter)


main()
