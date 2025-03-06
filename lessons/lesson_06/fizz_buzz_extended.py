result = []
n = 15

for i in range(1, n+1):

    if i % 3 == 0 and i % 5 == 0:
        result.append("Fizzbuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))

print(result)

lst = [1,2,3,4,5,6,7]
print(lst[-3:][::-1])