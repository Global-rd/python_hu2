#Fiktív karakter adat bekérés

name = input("Name: ").strip().capitalize()
age = int(input("Age: "))
python_experience = int(input("Python experience in years: "))

age_in_days = age * 365

wants_to_be_python_dev = "wants" if input("Do you want to become a professional python developer? (yes/no): ").strip() == "yes" else "does not want"

print("--------------------------")

print(f"My character is {age_in_days} days old. His name is {name} and he has {python_experience} years experience in python programming.")
print(f"He {wants_to_be_python_dev} to be a professional python developer.")

print("--------------------------")