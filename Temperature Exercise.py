def main():
    ENTER_TEMP_IN_CELSIUS = "Enter temperature in Celsius >> "
    TEMP_IN_CELSIUS = "'{}C is {}f'"

    myTemp = float(input(ENTER_TEMP_IN_CELSIUS))

    farenheight_temp = (9 / 5 + myTemp) + 32

    print(TEMP_IN_CELSIUS.format(myTemp, farenheight_temp))
    print("The temperature in C is", myTemp)

    main()
