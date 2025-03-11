def greet(name): #PARAMTER
    print(f"Hello {name}")

greet("Johnny") #ARGUMENT

#positional parameters

def add(x,y):
    return x+y

result = add(6, 5)
result = add(x=6, y=5)

#default argument
print("------------")
def greet_again(name="Guest"): #PARAMTER
    print(f"Hello {name}")

greet_again("Alice")
greet_again()

#combining positional, default arguments
print("--------------------")
def show_book_details(title, author="Test Writer", year=2025):

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("Test Book")
show_book_details("Test Book", "XY")
show_book_details("Test Book", "XY", 2014)


print("---------------------")
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} name {pet_name}")

describe_pet("Max", animal_type="cat")
describe_pet("Max")


def power(base, exponent, /, *, precision = None):

    result = base ** exponent
    if precision:
        return round(result, precision)
    return result

print(power(2.3, 3))
print(power(2.3, 3, precision=2))


#MUTABLE OBJECTS AS DEFAULT ARGUMENTS:
#bad example
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

#[1]
#[2]

# good example
print("------------------")
def append_to_list(value, my_list=None):

    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))