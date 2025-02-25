fruit = "raspberry"
fruit_length = len(fruit)
print(fruit_length)

#concatenation
first_name = "Istvan Gabor"
last_name = "Nagy"

full_name = first_name + " " + last_name
print(full_name)
introduction = "My name is " + first_name + " " + last_name + "."
print(introduction)

#interpolated string / f-string
introduction = f"My name is {first_name} {last_name}."
print(introduction)
print("-----------------------")
# indexing, slicing
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[-1])

print(fruit[1:3]) #1: inclusive, 3: exclusive
print(fruit[3:])
print(fruit[-2:])
print(fruit[-1::-2])


# string metódusok
#metódus: az amit az objektum tud csinálni
#attribútum: az ami jellemzi az objektumot

#objektum: kutya
#metódus: ugat, eszik, iszik, alszik
#attribútum: életkor, fajta, testsúly, név

print("-------------")
print(fruit)
print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())

print(fruit.replace("a", "#"))

fruit = "     apple     "
print(fruit.strip())

print(fruit.upper()
           .replace("A", "#")
           .strip()) #method chaining