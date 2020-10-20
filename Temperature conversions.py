"""
    This code is used for converting temperatrue between Celsius, Kelvin and Farenhait.
    User inputs a temperature, then he chooses a conversion option.
    Output example ( input was 10, option 1 was selected Celsious to Kelvin
    10 C = 283 K
    
"""

def menu():  
    """
       This is a function that writes out the options and returns value from 1 to 66.

    """
    print("""
    (1) Celsius to Kelvin
    (2) Celsius to Farenheit
    (3) Kelvin to Celsius
    (4) Kelvin to Farenheit
    (5) Farenheit to Celsius
    (6) Farenheit to Kelvin
    """)
    while True:
        try:
            option = int(input("Choose an option"))
            if option in [1, 2, 3, 4, 5, 6]:
                break
            else:
                raise ValueError()
        except ValueError:
            print("You must input a number between 1- and 6!!")

    return option


def write_conversion(unit_input, temp_unit, unit_output, temp_output):

    degree_sign = u"\N{DEGREE SIGN}"
    print(
        f"{temp_unit} {degree_sign} {unit_input} = {temp_output} {degree_sign} {unit_output}")


def kelvin_check(temp):
    if temp < -273.15:
        print("Bad input, under apsolute zero! (-273.15C)")
        exit(1)


def celsius_to_kelvin(temp):
    kelvin_check(temp)
    kelvin = temp + 273
    return kelvin


def celsius_to_farenheit(temp):
    kelvin_check(temp)
    farenhait = round(9 / 5 * temp + 32)
    return farenhait


def kelvin_to_celsius(temp):
    if temp < 0:
        print("Bad input,under absolute zero! ( 0K )!")
        exit(1)
    else:
        celsius = round(temp - 273)
        return celsius


def kelvin_to_farenhait(temp):
    if temp < 0:
        print("Bad input,under absolute zero! ( 0K )!")
        exit(1)
    else:
        farenhait = round(9 / 5 * temp - 459.67)
        return farenhait


def farenhait_to_celsius(temp):
    if temp < -459.67:
        print("Bad input,under absolute zero ( -459.67F)! ")
        exit(1)
    else:
        celsius = round(5 / 9 * (temp - 32))
        return celsius


def farenhait_to_kelvin(temp):
    if temp < -459.67:
        print("Bad input,under absolute zero ( -459.67F)! ")
        exit(1)
    else:
        kelvin = round(5 / 9 * (temp - 32) + 273)
        return kelvin


option = menu()

temp = float(input("Enter how many degrees you want to convert: "))
if option == 1:
    result = celsius_to_kelvin(temp)
    write_conversion("C", temp, "K", result)
elif option == 2:
    result = celsius_to_farenheit(temp)
    write_conversion("C",temp, "F", result)
elif option == 3:
    result = kelvin_to_celsius(temp)
    write_conversion("K",temp, "C", result)
elif option== 4:
    result = kelvin_to_farenhait(temp)
    write_conversion("K", temp, "F", result)

elif option == 5:
    result = farenhait_to_celsius(temp)
    write_conversion("F", temp, "C", result)
elif option == 6:
    result = farenhait_to_kelvin(temp)
    write_conversion("F",temp, "K", result)
