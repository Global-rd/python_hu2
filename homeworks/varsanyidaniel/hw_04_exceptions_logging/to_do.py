def read():
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/.txt" , "r") as file:
        print(file)
        """lines = file.readlines()
        print(lines)
        for line in lines:
            print(line.strip())"""




def display_menu ():
    print("\n 1. Add Task \n 2. Read Tasks \n 3 Remove Tasks \n 4. Exit \n")


while True:
    display_menu()
    try:
        option=int(input("Mondd meg, mit választasz: "))
    except ValueError:
        print("\n Csakis 1, 2, 3 vagy 4 -est választhatsz! \n")
    else:
        if option == 1:
            print("2")
        elif option == 2:
            read()
        elif option == 3:
            print("2")
        elif option == 4:
            print("2")
            break
        else:
            print("\n Csakis 1, 2, 3 vagy 4 -est választhatsz! \n")