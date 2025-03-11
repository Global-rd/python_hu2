# if number is divisible by 3 AND 5: FizzBuzz
# if number is divisible by 3 ONLY: Fizz
# if number is divisible by 5 ONLY: Buzz
# else: number as a string

n = 15

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))

#rossz példa
print("-------------")

if n % 3 == 0:
    print("Fizz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))
