"""
FELADAT

Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni (mintázhatod
nyugodtan magadról is :)). A feladatod, hogy a felhasználótól bekérd a
következő input-okat (ezeknek megfelelő, leíró változóneveket adj):

● Név
● Életkor
● Python tapasztalat években

A tanultak alapján kódold le, hogy a beírt név minden esetben nagy betűvel
legyen eltárolva a változóban, és szóköz se előtte, se utána ne szerepeljen.
Az életkort konvertáld át a megfelelő adattípusra, és egy új változóban tárold
el hogy mennyi idős a karakter napokban (Kerekíts az években megadott
életkor alapján, tételezzük fel hogy ma van az illető szülinapja).
Printeld ki az összes információt egy interpolált string-ben (f-string). A
végeredmény valami ilyesmi kell hogy legyen: 

"My character is
<age_in_days> old. His/her name is <name> and he/she has
<python_exp_in_years> years experience."

Extra feladat (szorgalmi):
Kérd be inputként a felhasználótól, hogy szeretné-e hogy a karaktere profi
Python fejlesztő legyen. Erre a válasz "yes" vagy "no" kell hogy legyen (az
inputok validálást később tanuljuk). Nézz utána a ternary operator-oknak
Python-ban, és tárold el ezt a változót egy boolean típusú változóban. Ezután
add hozzá a végső kiprintelendő f-string-hez. A végeredménynek ekkor így
kell kinéznie:

"My character is <age_in_days> old. His/her name is
<name> and he/she has <python_exp_in_years> years
experience. He/she wants to be a Python developer!"
Vagy
"My character is <age_in_days> old. His/her name is
<name> and he/she has <python_exp_in_years> years
experience. He/she does not want to be a Python
developer!"
"""

# Alap változók és érték megadásaik, hogy ne fusson hibára a program, ha a felhasználó nem jó adatot ad meg

user_name = ""
user_age = 0
python_exp_in_years = 0
final_text = ""
profi_python = False

# Extra feladat, ha true, akkor kiírja a második változatot és bekéri a plusz infót, ha false akkor nem 
is_extra = True

# Adatok beolvasása
input_name = input("Add meg a nevedet: ")
input_age = input("Hány éves vagy: ")
input_python_exp = input("Hány éve foglalkozol a Python programozással: ")

if is_extra:
    input_extra = input("Szeretnél profi programozó lenni Python nyelvben (yes/no): ") 
    # a beolvasott érték ellenőrzése,  ahol csak azt ellenőrzöm, hogy yes van-e beírva
    if input_extra.isprintable():
        if input_extra.lower() == "yes":
            profi_python = True
        

# A bejövő adatok ellenőrzése és modifikálása a megadás szerint

if input_name.isprintable():
    user_name = input_name.strip()
    user_name = user_name.lower()
    user_name = user_name.capitalize()

if input_age.isnumeric():
    user_age = int(input_age)
    age_in_days = user_age * 365 
    # szökő években plusz egy nap, tavaly volt szökőév ezért a -1
    age_in_days += (user_age-1) // 4

if input_python_exp.isnumeric():
    python_exp_in_years = int(input_python_exp)


# Megalkotni a végleges szöveget a kiíratáshoz
if is_extra:
   if profi_python:
       final_text = f"My character is {age_in_days} days old. His/her name is {user_name} and he/she has {python_exp_in_years} years experience. He/she wants to be a Python developer!"
   else:
       final_text = f"My character is {age_in_days} days old. His/her name is {user_name} and he/she has {python_exp_in_years} years experience. He/she does not want to be a Python developer!"   
else:
    final_text = f"My character is {age_in_days} days old. His/her name is {user_name} and he/she has {python_exp_in_years} years experience."


print(final_text)
