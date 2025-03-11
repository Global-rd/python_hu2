import time
numbers = [1, 2, 3, 4, 5]

#without list comprehension
squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

#list comprehension

squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

#without list comprehension
even_squares = []

for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)

print(even_squares)


#list comprehension

even_squares = [number ** 2 for number in numbers if number % 2 == 0]

print(even_squares)

numbers = range(1, 1000000000)

start = time.time()
squares_loop = []

for num in numbers:
    squares_loop.append(num ** 2)

print(f"For loop: {time.time() - start}")

start = time.time()
squares_comprehension = [num ** 2 for num in numbers]
print(f"comprehension: {time.time() - start}")
