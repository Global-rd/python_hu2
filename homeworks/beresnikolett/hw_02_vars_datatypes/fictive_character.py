character_info = { 
      "name": str(input("Name: ").capitalize().strip()),
      "age": int(input("Age: ")),
      "python_experience": int(input("Specify your years of experience with Python: ")),
    }
age_in_days= character_info["age"] * 365
print(f"My character is {age_in_days} old. His/Her name is {character_info['name']} and has {character_info['python_experience']} years of experience.")


