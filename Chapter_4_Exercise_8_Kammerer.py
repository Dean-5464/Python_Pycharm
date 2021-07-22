def main():

    # Sum Default Value (0)
    number_sum = 0

    # First Number Value
    user_response = float(input("Please Input Your First Number >> "))

    while user_response >= 0:
        number_sum = number_sum + user_response
        user_response = float(input("Please Enter Your Next Number >> "))

    print("Your Sum is", number_sum)


main()
