# Python weight converter :)

weight = float(input("Enter your weight: "))
choose = (input("Kilograms or Pounds? (K or L): "))

if choose.upper() == "K":
    res = weight * 2.205
    print(f"Your weight is: {round(res, 2)} Kgs.")
elif choose.upper() == "L":
    res = weight / 2.205
    print(f"Your weight is: {round(res, 2)} Lbs.")
else :
    print(f"{choose} is not valid!")

