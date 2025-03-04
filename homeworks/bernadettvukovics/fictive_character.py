name = input("What is Your character name? ").strip().upper()  # Name to UPPER and removes any leading and trailing whitespace.
age = int(input("How old? "))  # age convert to integer
python_exp = float(input("How many years of Python experience does your character have? "))  # Python experience input

# 2. Feladat:   Guess, it's Your birthday today, converting data. Konvertáljuk az életkort napokra (tételezzük fel, hogy ma van a szülinapja)
age_in_days = age * 365  

# 3. Feladat: So You are a professonal Python developer?
wants_to_be_developer = input("Szeretnéd, hogy a karaktered profi Python fejlesztő legyen? (yes/no) ").lower()
is_python_dev = True if wants_to_be_developer == "yes" else False  # Ternary operator use

# 4. Feladat: f-string use and print
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp} years experience.")
print(f"He/she wants to be a Python developer!" if is_python_dev else "He/she doesn't want to be a Python developer.")