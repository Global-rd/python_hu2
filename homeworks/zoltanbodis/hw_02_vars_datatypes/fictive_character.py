import functions

# name
name = input("What is your name? ").strip().capitalize()

# age
age = int(input("What is your age? "))

# Python experience években
# python_exp = int(input("How many years of experience have you in Python? "))
while True:
    python_exp = input("How many years of experience have you in Python: ")
    try:
        if "," in python_exp:
            python_exp = python_exp.replace(",",".")    
        float(python_exp)
        break
    except ValueError:
        continue

# Akar-e pro lenni PYthonban
wannabe_pro_input = input("Do you want to become a professional Python developer (yes or no)? ")
is_wannabe_pro = True if wannabe_pro_input == "yes" else False
#wannabe_pro_output = "He/she wants to be a Python developer!" if is_wannabe_pro else "He/she does not want to be a Python developer!"
wannabe_pro_output = "wants" if is_wannabe_pro else "does not want"

# életkor napokban, feltételezve, hogy ma van a szülinapja 
"""
Bocs, itt magával ragadott a hév, kiváncsi voltam, hogy lehet Pythonban dátumokkal dolgozni, úgyhogy nézegettem kicsit a datetime modult.
Viszont mivel folyton elkapkodom a teszteket, ezért gondoltam, megcsinálom a kért kerekítős módszerrel is, nehogy pontot veszítsek emiatt is :). 
És akkor már megnéztem, hogy kell ezt kirakni egy függvénybe.
"""
print(f"My character is {functions.f_age_in_days(age, 1)} (~ {functions.f_age_in_days(age, 2)}) days old. His/her name is {name} and he/she has {python_exp} years experience. He/she {wannabe_pro_output} to be a Python developer!")


