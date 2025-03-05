print("A következő kérdésekben egy fiktív karaktert fogsz létrehozni.\n")
név=input("Add meg egy nevét: ").strip().title()
kor=int(input("Add meg az életkorát: "))
tap=int(input("Mondd meg, hogy hány évnyi tapasztalata legyen python-ban: "))
question=input("Szeretnéd, hogy a karaktered profi python fejlesztő legyen? (yes ; no): ").strip()

print()

if question == "yes" or question == "no":

    if question == "yes":
        bquestion=bool(question)                     #itt azért nem csak True, mert mivel tudjuk, hogy a 'question' az 'yes' , ezért úgyis True -vá fogja alakítani a bool()
    elif question == "no":
        bquestion=False
    
    napkor=kor*365.25//1

    if bquestion == True:
        print(f"{név} is {kor} years, or {napkor} days old. He/She has {tap} years of python experience and he wishes to be a python developer.")
    if bquestion == False:
        print(f"{név} is {kor} years, or {napkor} days old. He/She has {tap} years of python experience, but does not wish to be a python developer.")


else:
    print("A 4. kérdésre csakis 'yes' vagy 'no' válasszal válaszolhatsz.")