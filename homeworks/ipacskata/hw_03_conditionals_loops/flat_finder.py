city = input("Enter the city in which you have the property").strip().title()
rent = int(input("Enter the amount of monthly rent"))

if city == "Washington":
    result = f"Sarah wouldn't live there for the life of her"
elif city in ["New York", "San Francisco"] and rent <4000:
    result= f"Sarah would like to live here"   
elif city == "Chicago":
    result=f"Sarah would definitely want to live here!" 
elif rent<3000:
    result = f"Sarah would be ok to move here"
else:
    result = f"Sarah wouldn't move here"

print(result)                
