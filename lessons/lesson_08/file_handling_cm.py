import os
print(os.getcwd())

file = open("lessons/lesson_08/sample.txt", "w") #relative path

#WITHOUT CONTEXT MANAGERS
try:
    file.write("This is a sample text")
finally:
    file.close()

#WITH CONTEXT MANAGERS:
with open("lessons/lesson_08/sample.txt", "w") as file:
    file.write("This is a sample text from the context manager!\n")

#WITH CONTEXT MANAGERS -APPEND:
with open("lessons/lesson_08/sample.txt", "a") as file:
    file.write("This is a sample text from the context manager!\n")

#FILE HANDLING : READING A FILE

with open("lessons/lesson_08/sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

# GENERATOR TO READ A FILE
print("--------------------")
def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


file_path = "lessons/lesson_08/sample.txt"
gen = read_file_line_by_line(file_path=file_path)
print(next(gen))
print(next(gen))

for line in read_file_line_by_line(file_path=file_path):
    print(line)
