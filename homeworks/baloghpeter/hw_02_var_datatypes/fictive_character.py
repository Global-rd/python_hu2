name = input("What is your name: " ).strip().upper()
age = int(input("How old are you: " ))
python_exp_in_years = int(input("How many years of python programming experience do you have: "  ))
age_in_days = age * 365
print("---------------")
print(f"My character is {age_in_days} old. His name is {name} and he has {python_exp_in_years} years expereince.")
