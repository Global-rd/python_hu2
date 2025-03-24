def read():
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/.txt" , "r") as file:
        for line in file.readlines():
            print(line.strip())


def add(addition):
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/.txt" , "a") as file:
        file.write(addition , "\n")


def remove():


def display_menu():
    print("\n 1. Add Task \n 2. Read Tasks \n 3 Remove Tasks \n 4. Exit \n")

display_menu()
while True:
    try:
        option=int(input("Mondd meg, mit választasz: "))
    except ValueError:
        print("\n Csakis 1, 2, 3 vagy 4 -est választhatsz! \n")
    else:
        if option == 1:
            addition=input("Írd le, hogy milyen teendőt szeretnél hozzáadni a programhoz:")
            add(addition)
        elif option == 2:
            read()
        elif option == 3:
            print("2")
        elif option == 4:
            break
        else:
            print("\n Csakis 1, 2, 3 vagy 4 -est választhatsz! \n")
            display_menu()