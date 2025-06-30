from ftplib import print_line

# or operator 1 or 0 = 1

temp = float(input("Please enter the temperature: "))
is_raining = False # or True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is still scheduled!")

# and operator 1 and 0 = 0
temp = 0
is_Sunny = True

if temp >= 28 and is_Sunny:
    print_line("It is HOT outside!")
    print_line("It is Sunny!")
elif temp <= 0 and is_Sunny:
    print_line("It is cold outside!")
    print_line("It is sunny!")
elif 28 > temp > 0 and is_Sunny:
    print_line("It is warm outside!")

# and not operator
temp = 20
is_Sunny = False

if temp >= 28 and not is_Sunny:
    print_line("It is HOT outside!")
    print_line("It is cloudy!")
elif temp <= 0 and not is_Sunny:
    print_line("It is cold outside!")
    print_line("It is cloudy!")
elif 28 > temp > 0 and not is_Sunny:
    print_line("It is warm outside!")
    print_line("It is cloudy!")

