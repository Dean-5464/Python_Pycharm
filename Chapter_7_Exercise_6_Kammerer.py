def larger(value, listed_numbers):

    larger_list = []

    for list_item_number in range(0, 11):
        if listed_numbers[list_item_number] > value:
            larger_list.append(listed_numbers[list_item_number])

    return larger_list


def main():
    value = 5
    listed_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(larger(value, listed_numbers))


main()
