# User Input
name = input("Please enter your character's name: ").strip().upper()
age = input("Please enter your character's age: ").strip()
python_exp_in_years = input(
    "Please enter your character's Python experience in years: "
).strip()

# convert age to integer and convert it to days
# (approximate - 365 days in a year)
age_in_days = int(age) * 365

# Extra challenge: ask the user whether (s)he wants her/his character to become
# professional in Python
wants_to_be_pro_in_python = (
    input("Do you want your character to become a professional in Python? (yes/no): ")
    .strip()
    .lower()
)

# introduce a ternary operator to store the answer in a boolean variable
is_pro = True if wants_to_be_pro_in_python == "yes" else False

# Output
message = (
    f"My character is {age_in_days} days old. Her/his name is {name}. "
    f"(S)he has {python_exp_in_years} years of Python experience. "
    f"(S)he {'wants' if is_pro else 'does not want'} to become a pro in Python."
)

print(message)
