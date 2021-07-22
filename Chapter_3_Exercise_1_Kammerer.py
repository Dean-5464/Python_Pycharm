# Chapter 3
# Exercise 1
# Dean Kammerer


def main():

    day = int(input("Please input an integer between 1 and 7 >> "))

    if day == 1:
        print("Day of the Week: Sunday")
    elif day == 2:
        print("Day of the Week: Monday")
    elif day == 3:
        print("Day of the Week: Tuesday")
    elif day == 4:
        print("Day of the Week: Wednesday")
    elif day == 5:
        print("Day of the Week: Thursday")
    elif day == 6:
        print("Day of the Week: Friday")
    elif day == 7:
        print("Day of the Week: Saturday")
    elif day < 1:
        print("Error: Value less than 1")
    elif day > 7:
        print("Error: Value greater than 7")


main()
