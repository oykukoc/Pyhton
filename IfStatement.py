# #First Example
from ftplib import print_line

# age = int(input(f"Welcome to the Game! Please enter your age before you continue : "))
#
# print(age)
# while age <= 0:
#         print("The age can not be negative or zero!")
#         age =int (input("Please enter your age again : "))
# if age >= 18:
#     print("Enjoy the game..")
# else :
#     print("This game contains strong language and violence.. You must be at least 18 to play this game!")

# Second Exmaple
#
# print_line("List of drinks")
# print_line("1 - Vodka-Redbull")
# print_line("2 - Whiskey")
# print_line("3 - Beer")
#
# response = input("Would you like to drink some Alcohol? (Y/N) : ")
#
# while response != "Y" and response != "y" and response != "N" and response != "n" and response != " ":
#     print("Please give a valid answer!")
#     response = input("Would you like to drink some Alcohol? (Y/N) : ")
# if response == "Y" or  response ==  "y":
#     chooseDrinks = int(input("Please enter a the number according the drinks, that you would like to drink : "))
#     while chooseDrinks != 1 and chooseDrinks != 2 and chooseDrinks != 3:
#         print_line("List of drinks")
#         print_line("1 - Vodka-Redbull")
#         print_line("2 - Whiskey")
#         print_line("3 - Beer")
#         chooseDrinks = int(input("Please enter the number of alcohol according to the table, that you would like to drink : "))
#     if chooseDrinks == 1:
#             print("Enjoy your Vodka-Redbull!")
#     elif chooseDrinks == 2:
#             print("Enjoy your Whiskey!")
#     else:
#             print("Enjoy your Beer!")
# else:
#     print("Have a nice day!")

#Second example improved version

print_line("List of drinks")
print_line("1 - Vodka-Redbull")
print_line("2 - Whiskey")
print_line("3 - Beer")

response = (input("Would you like to drink some Alcohol? (Y/N) : ")).lower()
while response != "y" and response != "n" and response != " " and response is not None:
    print("Please give a valid answer!")
    response = (input("Would you like to drink some Alcohol? (Y/N) : ")).lower()
if response ==  "y":
        print_line("List of drinks")
        print_line("1 - Vodka-Redbull")
        print_line("2 - Whiskey")
        print_line("3 - Beer")
        chooseDrinks = input("Please enter a the number according the drinks, that you would like to drink : ")
        while chooseDrinks == "" or not chooseDrinks.isdigit():
            print_line("List of drinks")
            print_line("1 - Vodka-Redbull")
            print_line("2 - Whiskey")
            print_line("3 - Beer")
            chooseDrinks = (input("Please enter the number of alcohol according to the table, that you would like to drink : "))
        chooseDrinks = int(chooseDrinks)
        while chooseDrinks > 3 :
                        chooseDrinks = int(chooseDrinks)
                        print_line("List of drinks")
                        print_line("1 - Vodka-Redbull")
                        print_line("2 - Whiskey")
                        print_line("3 - Beer")
                        chooseDrinks = int(input("Please enter the number of alcohol according to the table, that you would like to drink : "))
        if chooseDrinks == 1:
                            print("Enjoy your Vodka-Redbull!")
        elif chooseDrinks == 2:
                            print("Enjoy your Whiskey!")
        else:
                            print("Enjoy your Beer!")
else:
    print("Have a nice day!")
