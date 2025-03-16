#function without return value:
def greet_user(name):
    print(f"Hello {name}, welcome on board!")


value = greet_user("Alma")
print(value)
print(type(value))

#function with return value

def add(num_1, num_2):
    return num_1 + num_2

my_number = add(num_2=2,
                num_1=1)
print(my_number)

# return early
print("'-----------------------")
def calculate_age_in_days(age):
    if age < 0:
        print("Invalid age! Please provide a positive number!")
        return
    age_in_days = age * 365
    return age_in_days

age_in_days = calculate_age_in_days(-1)


#returning multiple values

def multiply_two_values(a, b):
    return a*2, b*2

print(type(multiply_two_values(1,2)))

x,y = multiply_two_values(1,2)
#(2,4)
print(x)
print(y)