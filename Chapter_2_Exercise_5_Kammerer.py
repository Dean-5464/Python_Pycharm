# Chapter 2
# Exercise 5
# Dean Kammerer


def main():

    print("Your speed is 70 Mi/Hr")
    speed = 70
    first_time = float(input("Please input the first time value >> "))
    second_time = float(input("Please input the second time value >> "))
    third_time = float(input("Please input the third time value >> "))

    first_distance = speed * first_time
    second_distance = speed * second_time
    third_distance = speed * third_time

    print("Your first distance traveled is", first_distance, "Mi")
    print("Your second distance traveled is", second_distance, "Mi")
    print("Your third distance traveled is", third_distance, "Mi")


main()
