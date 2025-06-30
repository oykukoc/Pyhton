
num = int(input("Please enter a number: "))

print("Positive" if num > 0 else "Negative")
result = "Even" if abs(num) % 2 == 0 else "Odd"
print(result)

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
maxNum = num1 if num1 > num2 else num2
print(maxNum)

age= int(input("Enter your age: "))
staus = "Adult" if age >= 18 else "Child"
print(staus)

userRole = input("Enter the access type: ")
accessLevel = "Full Access" if userRole == "admin" else "Limited Access"
print(accessLevel)