
# name = input("Enter your full name: ")
# phoneNumber = input("Enter your phone number: ")

# it does count the spaces too.
# result = len(name)

# the first occurrence of the given Char but starts with the index(0) numbers of the length
# result = name.find(" ")

# the last occurrence of the given Char but starts with the index(0) numbers of the length
# result = name.rfind("o")

#it capitalizes the first letter.
# result = name.capitalize()

# it capitalizes the whole letters
# result = name.upper()

# it turns the whole letters into lower cases
# result = name.lower()

# its boolean, returns True or False. It checks, if the given input only contains digits or not.
# result = name.isdigit()

#its boolean, returns True or False. It checks,  if the given input contains only letters or not.
# result = name.isalpha()

# it counts,how many characters input has
# result = phoneNumber.count(" ")

#it replaces the characters with the given char
# result = phoneNumber.replace(" ","-")

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Please enter a username: ")

while len(username) > 12 or any(char.isdigit() for char in username) or username.count(" ") != 0:
    print("Its not valid, try again!")
    username = input("Please enter a username again: ")

print(f"Welcome {username}!")