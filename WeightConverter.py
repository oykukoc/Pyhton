# Python weight converter :)

weight = float(input("Enter your weight: "))
choose = (input("Kilograms or Pounds? (K or L): "))

if choose.upper() == "K":
    result = weight * 2.205
    print(f"Your weight is: {round(weight, 2)} Kgs.")
elif choose.upper() == "L":
    result = weight / 2.205
    print(f"Your weight is: {round(weight, 2)} Lbs.")
else :
    print(f"{choose} is not valid!")

