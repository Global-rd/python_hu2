#syntax

condition = True

if condition == True:
    print("The condition is true")
else:
    print("The condition is false")

#truthy-falsy értékek

if condition:
    print("The condition is true")
else:
    print("The condition is false")

number = 1

if number:
    print(f"The value is greater than 0: {number}")
else:
    print("The value is 0")

# if-elif-else 
number = 14
print("--------------")
if number == 10:
    print(f"The number is 10")
elif number == 13:
    print(f"The number is 13")
elif number == 14:
    print(f"The number is 14")
else:
    print(f"The number is something different: {number}")

#using membership and logical operators
print("--------------------------------")

fruits = ["raspberry", "banana", "cherry", "watermelon"]

if "raspberry" in fruits:
    print("raspberry is present in fruits")

if "banana" not in fruits:
    print("banana is present in fruits")
else:
    print("banana is not present in fruits")


a = 1
b = 2
c = 3
if a is b:
    print("The 2 objects are the same by id")

#combining multiple operators

if (a is not b and c == 4) and ("cherry" in fruits or "elderflower" in fruits):
    print("OK")
else:
    print("NOT ok")