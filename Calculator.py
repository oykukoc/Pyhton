#Python Calculator

operator = input("Enter an operator (+ - * /): ")
while operator not in ["+","-","*","/"]:
    print(f"{operator} is not valid, please enter a valid operator! ")
    operator = input("Enter an operator (+ - * /): ")

num1 = input("Enter the first number: ")
while not num1.replace(".","").isdigit():
    print(f"{num1} is not valid, please enter a valid number! ")
    num1 = (input("Enter the first number: "))

num2 = input("Enter the second number: ")
while not num2.replace(".","").isdigit():
    print(f"{num2} is not valid, please enter a valid number! ")
    num2 = (input("Enter the second number: "))


num1 = float(num1)
num2 = float(num2)
if operator == "+":
                result = (num1) + num2
                print(result)
elif operator == "-":
                result = num1 - num2
                print(result)
elif operator == "*":
                result = num1 * num2
                print(result)
elif operator == "/":
                result = num1 / num2
                print(result)