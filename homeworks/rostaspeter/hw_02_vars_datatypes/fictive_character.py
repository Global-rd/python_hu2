#házi
name = input("Hogy hívnak?  ").upper().strip()
age = int(input("Hány éves vagy?  "))
experience = int(input("Hány év tapasztalatod van Pythonban?  "))
age_in_days = age*365

#szorgalmi
want_to = "wants" if input("Szeretnél professzionális Pythonista lenni? yes vagy no ") == "yes" else "does not want"
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience. He/she {want_to} to be a Python developer!")