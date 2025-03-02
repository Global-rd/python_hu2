import math

#assignment operator
fruit = "apple"
a = 10

a += 5
a = a + 5

#arithmetic operator

a = 10
b = 3

result = a + b # * - /
modulus = a % b
print(modulus)
square_root = a ** (1/2)
square_root = math.sqrt(a)
print(square_root)

#logical operator
print("--------")
a = True
b = False

print(a and b) #False
print(a or b) #True
print(not a)
print(not b)

#comparison operator
print("--------------------")
a = 10
b = 3

print(a > b)
print(a == b)
print(a != b)
print(a >= b)

# identity, membership, bitwise operator, ternary operator