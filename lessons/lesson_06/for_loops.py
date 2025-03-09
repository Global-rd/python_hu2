import time

songs = ["I'm a barbie girl", "8 óra munka", "Heavy is the crown", "I got options"]

for song in songs:
    print(f"Playing {song}")
    #time.sleep(2)
print("-------------")
student = {
    "name": "john",
    "age": 15,
    "spec": "computer science"
}

for k,v in student.items():
    print(f"Key: {k}, Value: {v}")

print("---------------")
for k in student.keys():
    print(k)

print("---------------")
for v in student.values():
    print(v)


#range
for id in range(0,5):
    print(id)

print(type(range(5)))

print(type(songs))