#VARIABLES / VÁLTOZÓK

name = "Jim"
age = 25

print(name)
age = 25 + 1
print(age)

camelCaseVariableName = "" #BAD PRACTICE PYTHON-BAN!!!
snake_case_variable_name = "" #GOOD PRACTICE PYTHON-BAN!!!

#KONSTANTSOK / CONSTANTS

PI = 3.14
MAX_ROUNDS = 3

# dynamically typed / dinamikus típusosság

#int x;
#x = 10;

x = 10
print(x)
x = "appletree"
print(x)

#reference (pointer)
print("-------------")
my_var = 15
my_var_2 = 15

print(id(my_var))
print(id(my_var_2))

#memória
# 15 -> my_var, my_var_2 

print("--------------")
x = 11
y = x #11

print(id(x))
print(id(y))
print(x)
print(y)

x = 10

print(id(x))
print(id(y))
print(x)
print(y)

#GARBAGE COLLECTION
x = 1000 # 1000's reference count: 1
x = 2000 # 1000's reference count: 0