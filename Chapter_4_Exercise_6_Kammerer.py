def main():

    print("Fahrenheit" + '\t' + "Celsius")
    print("__________________")

    for celsius in range(0, 21):
        fahrenheit = int((9/5) * celsius + 32)
        print(fahrenheit, '\t', celsius)


main()
