def main():
    room_number_dictionary = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
    instructor_dictionary = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
    time_dictionary = {"CS101": "8:00 A.M.", "CS102": "9:00 A.M.", "CS103": "10:00 A.M.", "NT110": "11:00 A.M.", "CM241": "1:00 P.M."}

    print("Course Numbers")
    print("CS101")
    print("CS102")
    print("CS103")
    print("NT110")
    print("CM241")

    user_input = input("Please Enter A course Number >>> ")

    print('Room number:', room_number_dictionary[user_input])
    print('Instructor:', instructor_dictionary[user_input])
    print('Start Time:', time_dictionary[user_input])


main()
