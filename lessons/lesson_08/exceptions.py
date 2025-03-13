def divide_numbers(a, b):
    return a / b

#ZERO DIVISION ERROR
result = divide_numbers(10,1) # eredetileg 0 volt
print(result)

#VALUE ERROR
#age = int(input("How old are you? (pleave provide a number)"))
#print(age)


# INDEX ERROR

my_list = [1,2,3,4,5]
print(my_list[0])
#print(my_list[5])

my_dict ={"a": 12,
          "b": 13}

#print(my_dict["c"])
print(my_dict.get("c", 0))

# built in exception list: https://www.w3schools.com/python/python_ref_exceptions.asp

try:
    a = float(input("First number:"))
    b = float(input("Second number"))
    c = a / b
except ValueError as e:
    print(f"Value error {e}")
except ZeroDivisionError as e:
    print(f"You can not divide by zero: {e}")
except Exception as e:
    print(f"Something unexpected happened: {e}")
else:
    print(c)
finally:
    print("Division attempt finished.")


print("valami")
print("---------------------")
# RAISE EXCEPTIONS

#bad example:
def calculate_rectangle_area(a,b):
    return a * b

area = calculate_rectangle_area(10, 5)
print(area)
area = calculate_rectangle_area(10, -2)
print(area)

# good example:
def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Both params must be a positive number!")
    return length * width

#calculate_rectangle_area(10, -2)

try:
    area = calculate_rectangle_area(5, -1)
except ValueError as e:
    print(f"Value error: {e}")


#custom exception
