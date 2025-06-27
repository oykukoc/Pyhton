
friends = 10
#friends = friends + 1
#friends += 1
#friends = friends ** 2
#remainder = friends % 3

x = 3.14
#result = round(y) #3
y = -4
#result = abs(y)
#result = pow(4,3) #64 = 4 x 4 x 4
z = 5
#result = max(x,y,z) # 5
#result = min(x,y,z) # 3.14

import math
x = 25
y = 9.1
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
result = math.sqrt(x) #5.0
result2 = math.ceil(y) #10
result2 = math.floor(y) #9

# C = 2 * pi * r
radius = float(input("Enter te radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The answer is : {round(circumference,2)} cm.")

#Hipotenüs = a^2 + b^2 = c^2
x = pow(float(input("Enter side A : ")),2)
y = pow(float(input("Enter side B : ")), 2)
z = math.sqrt(x + y)
print(f"Side C : {round(z , 2)}")