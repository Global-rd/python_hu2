print("A következő kérdésekben egy fiktív karaktert fogsz létrehozni.\n")
name=input("Add meg egy nevét: ").strip().title()
age=int(input("Add meg az életkorát: "))
experience=int(input("Mondd meg, hogy hány évnyi tapasztalata legyen python-ban: "))
qa=input("Szeretnéd, hogy a karaktered profi python fejlesztő legyen? (yes ; no): ").strip()

dayage=age*365.25//1 

if qa == "yes":
        bqa=bool(qa)                     #itt azért nem csak True, mert mivel tudjuk, hogy a 'question' az 'yes' , ezért úgyis True -vá fogja alakítani a bool()

elif qa == "no":
        bqa=False

else:
      bqa=None

if bqa == True:
    print(f"{name} is {age} years, or {dayage} days old. He/She has {experience} years of python experience and he wishes to be a python developer.")
if bqa == False:
    print(f"{name} is {age} years, or {dayage} days old. He/She has {experience} years of python experience, but does not wish to be a python developer.")
else:
    print("A 4. kérdésre csakis 'yes' vagy 'no' válasszal válaszolhatsz.")

