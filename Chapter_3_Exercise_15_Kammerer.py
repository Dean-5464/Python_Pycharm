# Chapter 3
# Exercise 15
# Dean Kammerer


def main():

    start_time = float(input("Please insert the amount of seconds >> "))

    if start_time < 60:
        print("Converted time is", start_time, "Seconds")

    elif start_time < 3600:
        converted_time_seconds = start_time % 60
        converted_time_minutes = int(start_time / 60)

        print("The converted time is", converted_time_minutes, "minutes and", converted_time_seconds, "seconds")

    elif start_time < 86400:
        converted_time_hours = int(start_time / 3600)
        converted_time_minutes = int((start_time % 3600) / 60)
        converted_time_seconds = ((start_time % 3600) % 60)

        print("Your converted time is", converted_time_hours, "Hours,", converted_time_minutes, "Minutes, and", converted_time_seconds, "Seconds")

    else:
        converted_time_days = int(start_time / 86400)
        converted_time_hours = int((start_time % 86400) / 3600)
        converted_time_minutes = int(((start_time % 86400) % 3600) / 60)
        converted_time_seconds = (((start_time % 86400) % 3600) % 60)

        print("Your converted time is", converted_time_days, "Days,", converted_time_hours, "Hours,", converted_time_minutes, "Minutes, and", converted_time_seconds, "seconds")


main()
