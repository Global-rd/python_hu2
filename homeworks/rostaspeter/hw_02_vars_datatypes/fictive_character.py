#házi
name = input("Hogy hívnak?  ").upper().strip()
age = int(input("Hány éves vagy?  "))
experience = int(input("Hány év tapasztalatod van Pythonban?  "))
age_in_days = age*365

#szorgalmi
want_to = True if input("Szeretnél professzionális Pythonista lenni? yes vagy no  ") == "yes" else False

if want_to:
    print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience. He/she wants to be a Python developer!")
else:
    print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience. He/she does not wants to be a Python developer!")