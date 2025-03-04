name = input("Írd be a neved: ").title()
age = input("Írd be az életkorodat években: ")
python_exp_in_years = input("Írd be hogy hány év tapasztalatod van python-ban: ")
pro_python_developer = input("Írd be hogy szeretnéd-e hogy a karaktered profi python fejlesztő legyen: ")

age_in_days = int(age) * 365

pro_python_developer = "wants" if pro_python_developer.lower() == 'yes' else "does not want"

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {pro_python_developer} to be a Python developer!")