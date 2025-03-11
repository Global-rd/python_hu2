from pprint import pprint

fictive_character = ()

fictive_character_name = input("Please give a name to the character: ")
fictive_character_age = input("Please give an age to the character: ")
fictive_character_pk = input("Please give a python knowledge in years to the character: ")
pprint(f"My character is {fictive_character_age} old. His/her name is {fictive_character_name.upper().strip()} and he/she has {fictive_character_pk} years experience. ")
print("------------------------------")

#Kiemelem az életkort, amit megszorzok 365, és hozzáadom a szökpéveket, mivel az osztás miatt float-ba rakja a szökőévet átalakítom int-be
age_in_day = fictive_character_age * 365
leap_year = fictive_character_age / 4
age_in_day = age_in_day + int(leap_year)

#Bekérek egy választ, amennyiben "igen"-t kapok, a python developer akar lenni a karakter, minden más esetben nem
question = input("Would you like your character to be a professional python developer? (Please only write 'yes' if he/she wants)")
prof_python = "wants" if question == "yes" else "does not want" 

#Kiemelem a nevet, majd az upper-el nagybetüssé alakítom, és strip-el leveszem a szóközöket
pprint(f"My character is {age_in_day} old. His/her name is {fictive_character_name.upper().strip()} and he/she has {fictive_character_pk} years experience. He/she {prof_python} to be a Python developer!")