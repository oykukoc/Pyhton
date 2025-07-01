# while(True)

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Welcome {name}")

food = input("Enter a food you like (q to quit): ")

# to escape from the while loop
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye!")

num = int(input("Enter a number between  1 - 10: "))
while num < 0 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between  1 - 10: "))
print("Your num is valid!")