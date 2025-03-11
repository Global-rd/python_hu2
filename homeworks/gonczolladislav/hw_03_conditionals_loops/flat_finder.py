# homework_03_conditionals_loops, task nr.1 using "if_elif_else, operators"

# intro
print("  This is a flat finder program for Sarah. ")
print("********************************************")

# inputs
city = input("Please enter the name of the city where the apartment is located. \n")
rent = int(input("Please indicate how much in $ you would rent the property for. \n"))

# list of cities
cities = ["New York", "San Francisco", "Washington", "Chicago"]

# logic
if city in cities:
    if city == "Chicago" and rent >= 0:
        case = "could"
    elif (city == "New York" or city == "San Francisco") and rent < 4000:
        case = "could"         
    else: 
        case = "wouldn't be able to"
elif city is not cities and rent <= 3000:
    case = "could"
else:
    case = "wouldn't be able to"

# printing the answer    
print(f"Sarah {case} move into the property in the {city} for ${rent} in rent.")
