name = input("What is your name: " ).lstrip().upper()
age = int(input("How old are you: " ))
python_exp_in_years = int(input("How many years of python programming experience do you have: "  ))
ageindays = age * 365
print("---------------")
print(f"My character is {ageindays} old. His name is {name} and he has {python_exp_in_years} years expereince.")
