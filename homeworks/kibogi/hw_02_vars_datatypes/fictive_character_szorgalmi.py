first_name = "   Bogi    "
last_name = "   Ki   "
name = (str.upper(f"{str.strip(first_name)} {str.strip(last_name)}"))
age = "43"
age_in_days = int(age) * 365
python_experience_year = "15"
motivation = input("Do you want to be a Python Developer?")
bool_map = {"yes": True, "no": False}
answer = bool_map.get(motivation)
answer1 = "She wants to be a Python developer!" if answer else "She does not want to be a Python developer :-("
szorgalmi_feladat = f"My caracter is {age_in_days} days old. Her name is {name} and she has {python_experience_year} years of experience. {answer1}"

print (szorgalmi_feladat)