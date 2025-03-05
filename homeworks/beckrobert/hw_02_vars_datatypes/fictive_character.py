name = str(input("What's your name?"))
age = int(input("How old are you?"))
python_experience = int(input("How many years of Python experience you have?"))


name_cap = name.capitalize()
name_final = name_cap.strip()


age_in_days = age *365


introduction = f"My character's name is {name_final}, he/she is {age_in_days} days old and he/she has {python_experience} years experience in Python"


print(introduction)
