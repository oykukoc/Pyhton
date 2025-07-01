
creditCard = "1234-56789-1345-6789"
for x in creditCard:
    print(x)

# from 1 to 11 but it increases 2
for x in reversed(range(1,11,2)):
    print(x)
print("Happy new year!")

# it does not include the 13
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)


