# Chapter 5
# Exercise 7
# Dean Kammerer


def calculate_seat_income(seat_cost, seats_sold):
    income = seat_cost * seats_sold
    return income


def calculate_seat_a_income(CLASS_A_SEATS, seats_a):
    income = CLASS_A_SEATS * seats_a
    return income


def calculate_seat_b_income(CLASS_B_SEATS, seats_b):
    income = CLASS_B_SEATS * seats_b
    return income


def calculate_seat_c_income(CLASS_C_SEATS, seats_c):
    income = CLASS_C_SEATS * seats_c
    return income


def calculate_total_income(seat_a, seat_b, seat_c):
    return seat_a + seat_b + seat_c


def main():
    CLASS_A_SEATS = 20
    CLASS_B_SEATS = 15
    CLASS_C_SEATS = 10

    seats_a = int(input("Enter the desired number of class A seats >> "))
    seats_b = int(input("Enter the desired number of class B seats >> "))
    seats_c = int(input("Enter the desired number of class C seats >> "))

    seat_a_income = calculate_seat_a_income(CLASS_A_SEATS, seats_a)
    seat_b_income = calculate_seat_b_income(CLASS_B_SEATS, seats_b)
    seat_c_income = calculate_seat_c_income(CLASS_C_SEATS, seats_c)

    total_income = calculate_total_income(seat_a_income, seat_b_income, seat_c_income)
    print("Income Generated: $" + str(total_income))


main()
