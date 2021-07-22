import random


def generated_number():
    return random.randint(1, 100)


def main():
    loop_break = False

    while not loop_break:

        user_answer = int(input("Select a number between 1 and 100 >> "))
        if user_answer < generated_number():
            print("Answer too low, try again")
            loop_break = False
        elif user_answer > generated_number():
            print("Answer too high, try again")
            loop_break = False
        else:
            print("Correct")
            loop_break = True


main()
