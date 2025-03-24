
# INPUT

first_name = input("First name:")
last_name = input("Last name:")
age = int(input("Age"))
python_experience = float(input("Python experience in years:"))

# MODIFIED INPUT

first_name_formatted = first_name.title().strip()
last_name_formatted = last_name.title().strip()
age_in_days = age * 365

# OUTPUT

print(first_name_formatted)
print(last_name_formatted)
print(age_in_days)
print(python_experience)

# OUTPUT IN ONE SENTENCE

print(f"{first_name_formatted} {last_name_formatted} is {age_in_days} days old with {python_experience} year(s) of Python experience.")