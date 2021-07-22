def main():

    number_string = ""

    for number in range(1, 101, 1):

        if number % 10 != 0:
            number_string = number_string + str(number) + ", "

        if number % 10 == 0:

            print(number_string)

            number_string = str(number) + ", Crackle, "

            if number == 100:
                print("100, Crackle")

        if number % 3 == 0:
            number_string = (number_string + "Snap, ")

        if number % 5 == 0:
            number_string = (number_string + "Crackle, ")

        if number % 7 == 0:
            number_string = (number_string + "Pop, ")


main()
