def main():

    size = 8

    for level in range(size, 0, -1):
        for line_number in range(level - 1):
            print('*', end='')
        print()


main()
