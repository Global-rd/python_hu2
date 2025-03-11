from pprint import pprint

student = {
    "name": "John",
    "age": 29,
    "grades": {"grammar": [1,2,3],
               "math": [3,4,5]},
    "major": "Computer Science",
    "is_active": True
}

pprint(student)

#accessing values

print(student["age"])
print(student["grades"]["grammar"][-1])

#accessing keys
print(student.keys())
print(type(student.keys()))

#accessing values
print(student.values())
print(type(student.values()))

student["name"] = "John Hopkins"
print(student)

student["grades"]["grammar"].append(1)
print(student)


#mapping table

us_grade_mapping = {
    5: "A",
    4: "B",
    3: "C",
    2: "D",
    1: "F"
}

latest_grade = int(input("Grade: "))
us_grade = us_grade_mapping[latest_grade]
print(us_grade)

