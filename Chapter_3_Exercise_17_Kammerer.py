# Chapter 3
# Exercise 17
# Dean Kammerer


def main():
    # Initial Feedback
    user_feedback = input("Please respond to all questions with either Yes or No, Can you read this? (Yes or No) >> ")

# First Solution (Stage 1)
    if user_feedback == "Yes":
        user_feedback = input("Try restarting your computer and try again. Did that work? (Yes or No) >> ")

# Second Solution (Stage 2)
        if user_feedback == "No":
            user_feedback = input("Try rebooting the router. Did that work? (Yes or No) >> ")

# Third Solution (Stage 3)
            if user_feedback == "No":
                user_feedback = input("Check the router and modem cables to ensure that there are no loose wires."
                                      " Did that work? (Yes or No) >> ")

# Fourth Solution (Stage 4)
                if user_feedback == "No":
                    user_feedback = input("Try moving the router to a different location."
                                          " Did that work? (Yes or No) >> ")

# Final Solution (stage 5)
                    if user_feedback == "No":
                        print("Unfortunately your router might be the problem, we advise you to purchase a new"
                              " router. Thank you for your time.")
                    elif user_feedback == "Yes":
                        print("Thank you for your time.")
                    else:
                        print("Input Error")

# End of Stage 4
                elif user_feedback == "Yes":
                    print("Thank you for your time.")
                else:
                    print("Input Error")

# End of Stage 3
            elif user_feedback == "Yes":
                print("Thank you for your time.")
            else:
                print("Input Error")

# End of Stage 2
        elif user_feedback == "Yes":
            print("Thank you for your time.")
        else:
            print("Input Error")

# End of Stage 1
    elif user_feedback == "No":
        print("Thank you for your time.")
    else:
        print("Input Error")


main()
