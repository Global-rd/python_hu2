#név,kor,python tapasztalat bekérése, számadatok azonnali integerré alakítása

name = input("What's your character's name?").strip().upper()
age = int(input("How old is your character?"))
python = int(input("How many years have you been programming in Python?"))

#életkor tárolása napokban egy változóban
age_days = age*365

#megkérdezzük, akare profi fejlesztő lenni
pro_python = input("Do you want to be a professional python developer? (yes/no): ").strip().lower()

#változó beállítása a ternary operator alapján
pro_python_yes = True if pro_python == "yes" else False

print("------------------------------")
#és most kiprinteljük fstringgel
print(f"My character is {age_days} days old. His/her name is {name} and he/she has {python} years experience. He/she {'wants' if pro_python_yes else 'does not want'} to be a Python developer!")

print("------------------------------")