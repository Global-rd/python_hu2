letters = ["a", "b", "a", "c", "d"]
print(letters)

mixed_type_list = ["a", True, 3, 3.14, None]
print(mixed_type_list)
print(type(mixed_type_list))

letters = []
print(letters)
letters = list()
print(letters)

#indexing

names = ["Sarah", "Jim", "Dexter"]
print(names[0])
print(names[:2])

numbers = list(range(1,10))
print(numbers)

names[0] = "Steve"
print(names)

names[:2] = ["Timmy", "Jeremy"]
print(names)

#inserting more
names[1:2] = ["Tarah", "Maria"]
print(names)

#inserting less
names[1:3] = ["Timmy"]
print(names)

#names[1:3] = "Timmy" #ne így!
print(names)

#methods

names.append("Cathlyn")
print(names)

#names.append(["Zeno", "Paula"])
#print(names)

names.extend(["Zeno", "Paula"])
print(names)

names.insert(2, "Jimmy")
print(names)

#remove items by value
names.remove("Jimmy")
print(names)

#remove items by index
names.pop(2)
print(names)

del names[1]

#full clearance of the list
names.clear()

chocolates = input("Give me your 3 favourite chocolates separated by a comma: ")
print(chocolates)
print(type(chocolates))

chocolates_list = chocolates.split(",")
print(chocolates_list)
print(type(chocolates_list))