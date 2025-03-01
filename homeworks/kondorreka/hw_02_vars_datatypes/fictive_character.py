# Feladat 1: Változók, user input, string metódusok, type conversion, f-string használata

from datetime import date
"""
Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni (mintázhatod
nyugodtan magadról is :)). A feladatod, hogy a felhasználótól bekérd a
következő input-okat (ezeknek megfelelő, leíró változóneveket adj):

● Név
● Életkor
● Python tapasztalat években

A tanultak alapján kódold le, hogy a beírt név minden esetben nagy betűvel
legyen eltárolva a változóban, és szóköz se előtte, se utána ne szerepeljen.
"""
your_name = input("Add meg a neved!").strip().title()

while True:

    age = input("Hány éves vagy?")

    try:
        age = int(age)
        print("Köszönöm!")
        break # kilépés a ciklusból

    except ValueError:
        print("Kérlek számjegyekkel, egész számként add meg a korod!")

while True:

    python_exp = input("Hány éve pythonozol?")

    try:
        python_exp = float(python_exp)
        break
    
    except ValueError:
        print("Kérlek számjegyekkel add meg hány éve pythonozol. pl. 1.5")


# Az életkort konvertáld át a megfelelő adattípusra, és egy új változóban tárold
# el hogy mennyi idős a karakter napokban (Kerekíts az években megadott
# életkor alapján, tételezzük fel hogy ma van az illető szülinapja).

birthday = date.today()

year_of_birth = birthday.year - int(age)

day_of_birth = date(year_of_birth, birthday.month, birthday.day)

age_in_days = (birthday - day_of_birth).days

# Printeld ki az összes információt egy interpolált string-ben (f-string). A
# végeredmény valami ilyesmi kell hogy legyen: "My character is 
# <age_in_days> old. His/her name is <name> and he/she has
# <python_exp_in_years> years experience."

print(f'My character is {age_in_days} days old. ' 
      f'His/her name is {your_name} and ' 
      f'he/she has {python_exp} years experience.')

# Extra feladat (szorgalmi):
# Kérd be inputként a felhasználótól, hogy szeretné-e hogy a karaktere profi
# Python fejlesztő legyen. Erre a válasz "yes" vagy "no" kell hogy legyen (az
# inputok validálást később tanuljuk). Nézz utána a ternary operator-oknak
# Python-ban, és tárold el ezt a változót egy boolean típusú változóban. Ezután
# add hozzá a végső kiprintelendő f-string-hez. A végeredménynek ekkor így
# kell kinéznie:

# "My character is <age_in_days> old. His/her name is
# <name> and he/she has <python_exp_in_years> years
# experience. He/she wants to be a Python developer!"
# Vagy
# "My character is <age_in_days> old. His/her name is
# <name> and he/she has <python_exp_in_years> years
# experience. He/she does not want to be a Python
# developer!""""

while True:
    future_plans = input("Szeretnél Python fejlesztő lenni? (yes/no) ").strip().lower()

    if future_plans == "yes":
        future_plans = True
        break
        
    elif future_plans == "no":
        future_plans = False
        break
        
    else:
        print("Kérlek, 'yes' vagy 'no' értéket adj meg.")


text = "wants to be" if future_plans else "does not want to be"

print(f'My character is {age_in_days} days old. His/her name is '
    f'{your_name} and he/she has {python_exp} years '
    f'experience. He/she {text} a Python developer!')


        
