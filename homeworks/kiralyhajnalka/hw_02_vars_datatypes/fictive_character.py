#1. feladat: adatok bekérése: Név, Életkor, Python tapasztalat években
name = input ("full name: ")
age_in_days = int(input("her ages: " ))
python_exp_in_years = int(input("year: " ))
introduction = f"My character is {age_in_days} old. Her name is {name.upper().strip()} and she has {python_exp_in_years} years experience."
print (introduction)

