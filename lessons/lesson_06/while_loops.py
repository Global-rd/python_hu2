import time
while True:
    answer = input("Do you want to be a prof. python developer? yes/no")
    if answer in ["yes", "no"]:
        break

print("---------")

#infinite loop
#while True:
#    print("infinite loop")
#    time.sleep(1)


count = 0
while count < 5:
    print(count)
    count += 1