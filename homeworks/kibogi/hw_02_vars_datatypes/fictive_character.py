"""
Kommentként itt hagyon az eredeti feladatomat javitás elöttröl, hogy tanuljak belöle:

first_name = "   Bogi    "
last_name = "   Ki   "
name = (str.upper(f"{str.strip(first_name)} {str.strip(last_name)}"))
age = "43" 
age_in_days = int(age) * 365
python_experience_year = "15"

exercice_1 = f"My caracter is {age_in_days} days old. Her name is {name} and she has {python_experience_year} years of experience."

print(exercice_1)

"""

first_name = input ("Add meg a keresztnevedet").strip().capitalize()
last_name = input ("Add meg a családnevedet").strip().capitalize()
age = input ("Add meg a korodat")
python_experience_year = input("Hány év Python tapasztalatod van?")
name = f"{first_name} {last_name}"
age_in_days = int(age) * 365

exercice_1 = f"My caracter is {age_in_days} days old. Her name is {name} and she has {python_experience_year} years of experience."

print(exercice_1)

#extra feladat
motivation = input("Do you want to be a Python Developer?")
bool_map = {"yes": True, "no": False}
motivation = bool_map.get(motivation)
answer1 = "wants" if motivation == True else "does not want"
extra_exercice = f"My caracter is {age_in_days} days old. Her name is {name} and she has {python_experience_year} years of experience. She {answer1} to be a Python developer!"

print (extra_exercice)