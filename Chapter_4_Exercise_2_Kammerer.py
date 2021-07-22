def main():
    cycle = 1

    burned_per_minute = 4.2

    cycle_1_time = 10
    cycle_2_time = 15
    cycle_3_time = 20
    cycle_4_time = 25
    cycle_5_time = 30

    while cycle < 6:

        # Cycle 1 Calories Burned (10 Minutes)
        if cycle == 1:
            burned_calories = cycle_1_time * burned_per_minute
            print(burned_calories)
            cycle = cycle + 1

        # Cycle 2 Calories Burned (15 Minutes)
        elif cycle == 2:
            burned_calories = cycle_2_time * burned_per_minute
            print(burned_calories)
            cycle = cycle + 1

        # Cycle 3 Calories Burned (20 Minutes)
        elif cycle == 3:
            burned_calories = cycle_3_time * burned_per_minute
            print(burned_calories)
            cycle = cycle + 1

        # Cycle 4 Calories Burned (25 Minutes)
        elif cycle == 4:
            burned_calories = cycle_4_time * burned_per_minute
            print(burned_calories)
            cycle = cycle + 1

        # Cycle 5 Calories Burned (30 Minutes)
        elif cycle == 5:
            burned_calories = cycle_5_time * burned_per_minute
            print(burned_calories)
            cycle = cycle + 1


main()
