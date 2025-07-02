# List = [] ordered and changeable. Duplicates OK.
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

#LIST
fruits = ["apple","orange","banana","coconut"]

# print(fruits[0:3]) #['apple', 'orange', 'banana']
# print(dir(fruits))
print("apple" in fruits) #True
print("pineapple" in fruits) #False

for x in fruits:
    print(x)

fruits[0] = "pineapple"
print("pineapple" in fruits) #True

# it adds a new stuff to the end of the List
fruits.append("watermelon")
print(fruits) #['pineapple', 'orange', 'banana', 'coconut', 'watermelon']

fruits.remove("orange")
print(fruits) #['pineapple', 'banana', 'coconut', 'watermelon']

fruits.insert(0,"apple")
print(fruits) #['apple', 'pineapple', 'banana', 'coconut', 'watermelon']


fruits.reverse()
print(fruits) #['watermelon', 'coconut', 'banana', 'pineapple', 'apple']

index = fruits.index("apple")
print(index) #4

count =fruits.count("banana")
print(count) #1

len = len(fruits)
print(len) #5

fruits.clear()
print(fruits) #[]

#SET
fruits = {"apple","orange","banana","coconut"}

fruits.add("strawberry")
print(fruits) #{'strawberry', 'apple', 'orange', 'banana', 'coconut'}

fruits.add("coconut")
print(fruits) #{'coconut', 'banana', 'apple', 'strawberry', 'orange'

# it deletes some random element from the table
fruits.pop()
print(fruits)

#TUPLE
fruits = ("apple","orange","banana","coconut","coconut")

print(fruits.index("orange")) #1

print(fruits.count("coconut")) #2

for fruit in fruits:
    print(fruits)
