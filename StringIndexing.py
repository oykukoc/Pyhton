#indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

creditNumber = "1234-4567-7998-3456"

#prints the 4th index
print(creditNumber[4])

# prints the 0 , 1 , 2 and 3'th indexes
print(creditNumber[0:4]) #1234
print(creditNumber[5:9]) #4567
print(creditNumber[5:]) #4567-7998-3456

# prints the number from the opposite direction of number (from back to front)
print(creditNumber[-2]) #5

#prints the numbers according to step number,which can divide by 2
print(creditNumber[::2]) #13-5779-46

lastDigits = creditNumber[-4:]
print(f"XXXX-XXXX-XXXX-{lastDigits}")

