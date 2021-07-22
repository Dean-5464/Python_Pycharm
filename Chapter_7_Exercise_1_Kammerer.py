def main():

    weekly_sales = []
    total = 0

    for day_of_the_week in range(0, 7, 1):

        print('Sales for Day number', day_of_the_week + 1)
        day_input = float(input("Please Input Your value >>> "))
        weekly_sales.append(day_input)

        total = total + day_input

    print(weekly_sales)
    print('Your Total Number of Sales is', total)


main()

