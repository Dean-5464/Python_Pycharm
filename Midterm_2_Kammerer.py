def main():

    end_loop = False
    user_input = ""
    while end_loop == False:

        print("Find A Menu Item or Button Which Looks Related to What You Want to Do")
        user_input = input("(I Can't Find One) or (Ok) >>> ")

        if user_input == "I Can't Find One":

            user_input == input("Pick One at Random (I've Tried Them All, or Ok) >>> ")

            if user_input == "I've Tried Them All":
                user_input = input("Google The Name of The Program Plus a Few Words Related to What You Want to Do. Follow Any Instructions. Did it Work? (Yes or No) >>> ")

                if user_input == "Yes":
                    print("You're Done")
                    end_loop = True

                else:

                    user_input = input("Have You Been Trying This for Over Half an Hour? (Yes or No) >>> ")

                    if user_input == "Yes":
                        print("Ask Someone for Help or Give Up")
                        end_loop = True

            elif user_input == "Ok":

                user_input = input("Click it, Did it Work? (Yes or No) >>> ")

                if user_input == "Yes":
                    print("You're Done")
                    end_loop = True

                else:

                    user_input = input("Have You Been Trying This for Over Half an Hour? (Yes or No) >>> ")

                    if user_input == "Yes":
                        print("Ask Someone for Help or Give Up")
                        end_loop = True

        else:

            user_input = input("Click it, Did it Work? (Yes or No) >>> ")

            if user_input == "Yes":
                print("You're Done")
                end_loop = True

            else:

                user_input = input("Have You Been Trying This for Over Half an Hour? (Yes or No) >>> ")

                if user_input == "Yes":
                    print("Ask Someone for Help or Give Up")
                    end_loop = True


main()
