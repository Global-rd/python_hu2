#Fiktív karakter adat bekérés

name = input("Name: ").strip().capitalize()
age = int(input("Age: "))
python_experience = int(input("Python experience in years: "))

age_in_days = age * 365

become_developer = True if input("Do you want to become a professional python developer? (yes/no): ").strip() == "yes" else False

print("--------------------------")

print(f"My character is {age_in_days} days old. His name is {name} and he has {python_experience} years experience in python programing.")
print("He want to be a professional python developer." if become_developer else "He don't want to be a professional python developer.")

print("--------------------------")