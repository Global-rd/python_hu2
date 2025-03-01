fictive_character = {
    "name" : "  John Doe  ",
    "age" : 36,
    "python_knowledge" : 2,
}

#Kiemelem az életkort, amit megszorzok 365, és hozzáadom a szökpéveket, mivel az osztás miatt float-ba rakja a szökőévet átalakítom int-be
age_in_day = fictive_character["age"] * 365
leap_year = fictive_character["age"] / 4
age_in_day = age_in_day + int(leap_year)

#Kiemelem a nevet, majd az upper-el nagybetüssé alakítom, és strip-el leveszem a szóközöket
print(f"My character is {age_in_day} old. His/her name is {fictive_character["name"].upper().strip()} and he/she has {fictive_character["python_knowledge"]} years experience.")

#Bekérek egy választ, amennyiben "igen"-t kapok, a python developer akar lenni a karakter, minden más esetben nem
question = str(input("Would you like your character to be a professional python developer? (Please only write 'yes' if he/she wants)"))
prof_python = "wants" if question == "yes" else "does not want" 
print(f"He/she {prof_python} to be a Python developer!")