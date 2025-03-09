name = str(input("What's your name?")).capitalize().strip()
age = int(input("How old are you?"))
python_experience = int(input("How many years of Python experience you have?"))



age_in_days = age *365


introduction = f"My character's name is {name}, he/she is {age_in_days} days old and he/she has {python_experience} years experience in Python"


print(introduction)
