number = 15


def print_screen():
    # Number is scoped to print_screen
    number = 10
    print(number)


def main():
    # Number is scoped to main

    number = 5
    for number in range(6, 10):
        print(number)

    print_screen()
    print(number)


main()
