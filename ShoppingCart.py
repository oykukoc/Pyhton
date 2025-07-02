
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    lowered = food.lower()
    if lowered == "q":
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(price)

print("The shopping list: ")
for food,price in zip(foods,prices):
    print(f"{food} -> {price}$")

for p in prices:
    p = float(p)
    total += p
print(f"Total count is : {total}")
