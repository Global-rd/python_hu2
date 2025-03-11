name = input("A karaktered neve: ").strip().upper()
age = int(input("A karaktered eletkora: "))
python_exp_in_years = int(input("A karakter Python tapasztalata evekben: "))
age_in_days = int(age * 365)
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")
#szorgalmi:
wants_to_be_python_dev = input("Szeretnel-e profi Python fejleszto lenni (yes/no): ").strip().lower()
is_python_dev = True if wants_to_be_python_dev == 'yes' else False


print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")
if is_python_dev:
    print("He/she wants to be a Python developer!")
else:
    print("He/she does not want to be a Python developer!")