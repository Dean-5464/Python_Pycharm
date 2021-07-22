def main():

    email_dictionary = {"A": "A@Test.com", "B": "B@Test"}

    end_loop = False

    while end_loop == False:

        print('Names and Email Addresses')
        print("1.) Look Up an Address")
        print("2.) Add Name or Address")
        print("3.) Change an Existing Address")
        print("4.) Delete an Address" '\n')

        user_input = int(input("Please Enter Your Decision >>> "))

        if user_input == 1:
            name = input("Please Enter A Name >>> ")
            print(email_dictionary.get(name), '\n')
            end_input = input("Continue? (Y or N) >>> ")
            if end_input == "N":
                end_loop = True

        elif user_input == 2:
            name = input("Please Enter a Name >>> ")
            email = input("Please Enter an Email >>> ")

            if name not in email_dictionary:
                email_dictionary[name] = email
            else:
                print("Entry Already Exists")

            end_input = input("Continue? (Y or N) >>> ")
            if end_input == "N":
                end_loop = True

        elif user_input == 3:

            name = input("Please Enter the Name That You Want to Change >>> ")

            if name in email_dictionary:
                email = input("Please Enter the Updated Email Address >>> ")
                email_dictionary[name] = email
            else:
                print("Name Not Found")

            end_input = input("Continue? (Y or N) >>> ")
            if end_input == "N":
                end_loop = True

        if user_input == 4:
            name = input("Please Enter the Name that You Want to Delete >>> ")

            if name in email_dictionary:
                del email_dictionary[name]
                print("Done!")
            else:
                print("Name Not Found")

            end_input = input("Continue? (Y or N) >>> ")
            if end_input == "N":
                end_loop = True


main()
