"""This
is 
my
first
python
program 
""" 

example_variable1 = "string"
print(example_variable1)

example_variable2 = 1
print(example_variable2)

example_variable3 = 1.0
print(example_variable3)

example_variable4=None
print(example_variable4)

print(type(example_variable1))
print(type(example_variable2))
print(type(example_variable3))
print(type(example_variable4))

print(example_variable1, example_variable2, example_variable3, example_variable4)

print(example_variable1 + str(example_variable2)+ str(example_variable3)+ str(example_variable4))

print("first variable is a {example_variable1}, second variable is an integer: {example_variable2}, third variable is a float: {example_variable3}, fourth variable is a {example_variable4} variable".format(example_variable1=example_variable1, example_variable2=example_variable2, example_variable3=example_variable3, example_variable4=example_variable4))

#change the type of the variables
print("new type of the variables  :-) ")
example_variable1 = 100
example_variable2 = "string"
example_variable3 = None
example_variable4 = 1.0

print(type(example_variable1))
print(type(example_variable2))
print(type(example_variable3))
print(type(example_variable4))

print("first variable is a {example_variable1}, second variable is a: {example_variable2}, third variable is a {example_variable3} variable, fourth variable is a float: {example_variable4}".format(example_variable1=example_variable1, example_variable2=example_variable2, example_variable3=example_variable3, example_variable4=example_variable4))