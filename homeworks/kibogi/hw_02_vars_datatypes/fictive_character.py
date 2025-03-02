first_name = "   Bogi    "
last_name = "   Ki   "
name = (str.upper(f"{str.strip(first_name)} {str.strip(last_name)}"))
age = "43"
age_in_days = int(age) * 365
python_experience_year = "15"


feladat_1 = f"My caracter is {age_in_days} days old. Her name is {name} and she has {python_experience_year} years of experience."

print(feladat_1)