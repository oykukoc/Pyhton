# format specifiers = {value:flags} format a value based on wht flags are inserted.

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.3f}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.1f}")

# it has 10 spaces to display the output "^ means center" "< means to the left"
print(f"Price 3 is {price3:^10}")


