import random


def main():
    numbers = []

    for slot_number in range(0, 7, 1):
        generated_number = random.randint(0, 9)

        numbers.append(generated_number)


main()
