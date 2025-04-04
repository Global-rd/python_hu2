# input bekérése
nev = input("Add meg a karakter nevét:").strip().capitalize()
eletkor_evben = int(input("Add meg a karakter életkorát:"))
python_tapasztalat_evben = int(input("Add meg a karakter Python tapasztalatát: "))

# Életkor napokban
napokban_eletkor = eletkor_evben * 365

# Profi Python fejlesztő-e?
profi_valasz = input("Szeretnéd, hogy a karaktered profi Python fejlesztő legyen? (yes/no): ").strip().lower()
profi_python_fejleszto = True if profi_valasz == "yes" else False

# Eredmény kiírása
print(f"My character is {napokban_eletkor} days old. His/her name is {nev} and he/she has {python_tapasztalat_evben} years experience. Is he/she a professional Python developer? {profi_python_fejleszto}.")
