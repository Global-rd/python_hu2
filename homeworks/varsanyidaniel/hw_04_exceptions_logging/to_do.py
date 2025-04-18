import logging

file_handler = logging.FileHandler("homeworks/varsanyidaniel/hw_04_exceptions_logging/logs.log")
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def read():
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/tasks.txt" , "r") as file:
        print("\n")
        information = file.readlines()
        if information == []:
            return print("A feladatlista üres!")
        for i, line in enumerate(information, 0):                                                                   #for i, line in enumerate(file.readlines(), 0):
            print(f"{i+1}. - {line.strip()}")                                                                           #print(f"{i+1}. - {line.strip()}")


def add(addition):
    try:
        with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/tasks.txt" , "a") as file:
            if addition == "":
                return logging.warning("\nA feladatlistába nem rakhatsz üres elemeket!\n")
            file.write(f"{addition} \n")
    except Exception as error:
        logging.error(f"\nAn error has occured: {error}\n")


def remove(removable):
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/tasks.txt" , "r") as file:
        information = file.readlines()
    if information == []:
        logging.warning("\nA feladatlista üres!\n")
        return
    elif removable < 0 or removable > len(information):
        logging.warning("\nInvalid Number!\n")
        return
    information.pop(removable)
    with open("homeworks/varsanyidaniel/hw_04_exceptions_logging/tasks.txt" , "w") as file:
        file.writelines(information)



def display_menu():
    print("\n 1. Add Task \n 2. Read Tasks \n 3 Remove Tasks \n 4. Exit \n")


while True:
    display_menu()
    try:
        option=int(input("Mondd meg, mit választasz: "))
    except ValueError:
        logging.warning("\nCsakis 1, 2, 3 vagy 4 -est választhatsz!\n")
    else:
        if option == 1:
            addition=input("\nÍrd le, hogy milyen teendőt szeretnél hozzáadni a programhoz: ")
            add(addition)
        elif option == 2:
            read()
        elif option == 3:
            try:
                read()
                removable=int(input("\nMondd meg, hogy hanyadik feladatot szeretnéd kitörölni: "))-1
                remove(removable)
            except Exception as error:
                logging.error(f"\nAn error has occured {error}\n")
        elif option == 4:
            break
        else:
            logging.warning("\n Csakis 1, 2, 3 vagy 4 -est választhatsz!\n")