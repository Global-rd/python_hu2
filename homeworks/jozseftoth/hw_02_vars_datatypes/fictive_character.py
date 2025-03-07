#2nd homework with some cool stuff :-) 

name = input("Please enter your name: ").strip().upper()

age = input("Please enter your age in years: ")

python_exp_in_years = input("Please enter your python experience in years: ")
age_in_days = int(age) * 365


pro_python_developer_input = input("Do you want to be a professional python developer? /yes or no/: ")
pro_python_developer_input = pro_python_developer_input.lower()

if pro_python_developer_input == "yes":
    pro_python_developer = True
elif pro_python_developer_input == "no":
    pro_python_developer = False
else:
    print("HEY!!!! Your answer is not valid! I will decide for you! You are a Python developer! :-)")
    pro_python_developer = None 

print(f"Hey {name}! You are {age_in_days} days or {int(age)} years old.")
print(f"I know your name ;-) , and you have {python_exp_in_years} years experience.\nAnd cool, you want to be a Python developer! \nWELCOME ON BOARD!") if pro_python_developer else print(f"You have {python_exp_in_years} years Python experience. \nSo, I know you don't want to be a Python developer! \nGood bye and never come back!")