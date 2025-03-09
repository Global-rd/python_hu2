name = input("Give me your full name").strip().capitalize() #katalin ipacs
age = input("Give me your age in numbers") #45
python_experience = input("How long have you been working with Python? Answer in years (number)") #1
age_in_days = int(age)*365.25
introduction = f"My character is {age_in_days} old. Her name is {name} and she has {python_experience} year of experience."

print(introduction)

wish = input("Would you like to be a Python Grand Master? (yes/no)").strip().lower()
is_python_grand_master = True if wish =="yes" else False
print(is_python_grand_master)

introduction=f"My character is {age_in_days} old. Her name is {name} and she has {python_experience} "\
f"years of experience. She would like to become a Python Developer and that is {is_python_grand_master}."
print(introduction)
