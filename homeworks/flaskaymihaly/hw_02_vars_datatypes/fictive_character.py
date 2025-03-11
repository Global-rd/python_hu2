name=input("what is your name? ").title().strip()
age=int(input("How old are you? "))*365
experience=float(input("How long have you been using python? Please state in years! "))


print("--------------------------------------------------------------------------")
print(f"My character is", age,"days old. His name is", name, "and have", experience, "years of python experience.")
print("---------------------------------------------------------------------------")

#for extra points homework

extra_question=input(f"{name}, do you want to be a professional python developer?")
"""print("---------------------------------------------------------------------------")

if extra_question=="yes":
    print(f"My character is", age,"days old. His name is", name, "and have", experience, "years of python experience. He wants to be a python developer!")

elif extra_question=="no":
    print(f"My character is", age,"days old. His name is", name, "and have", experience, "years of python experience. He does not want to be a python developer!")

else:
    print("Sorry dude, you seem lost...")

ternary operator"""

print("---------------------------------------------------------------------------")
#ternary method

dev_intention="wants" if extra_question=="yes" else "does not want"

print(f"My character is", age,"days old. His name is", name, "and have", experience, "years of python experience. He", dev_intention, "to be a python developer!") 

