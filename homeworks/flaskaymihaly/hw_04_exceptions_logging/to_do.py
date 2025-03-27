

import logging



file_handler = logging.FileHandler("homeworks/flaskaymihaly/hw_04_exceptions_logging/to_do.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

file = open("homeworks/flaskaymihaly/hw_04_exceptions_logging/task_manager.txt", "w")


#------------------------------------------------------------------


def add_task(task_to_add):
    try:
        with open("homeworks/flaskaymihaly/hw_04_exceptions_logging/task_manager.txt", "a") as file:      
            file.write(f"{task_to_add}\n")
            print(f"{task_to_add} added")
    except FileNotFoundError as e:
        logging.error(f"Error to add task!: {e}")    
    

def read_task():
    try:
        with open("homeworks/flaskaymihaly/hw_04_exceptions_logging/task_manager.txt", "r") as file:       
            lines = file.readlines()
            if lines:
                for line in lines:
                    print(line.strip())
            else:
                logging.error("The file is empty!")
    except FileNotFoundError as e:
        logging.error(f"The file does not exist!: {e}")


def remove_task(task_to_remove):
    try:
        with open("homeworks/flaskaymihaly/hw_04_exceptions_logging/task_manager.txt", "w") as file:
            file.remove(task_to_remove)
            print(f"{task_to_remove} removed")
    except FileNotFoundError as e:
        logging.error(f"Error to remove task!: {e}")  


        

def display_menu():
    print("1. Add task")
    print("2. Read task")
    print("3. Remove task")
    print("4. Exit task")

def main():
    display_menu()
    while True:
        choose= int(input("What would you like to do? Pick a number: "))
         
        if choose==1:
            task_to_add=input("what task would you like to add?")
            add_task(task_to_add)
    
        elif choose==2:
            read_task()
    
        elif choose==3:
            task_to_remove=input("what task would you like to remove?")
            remove_task(task_to_remove)

        elif choose==4:
            print("Exited the application!")
            break
        else:
            print("invalid choice, please pick a number from the display menu!")

main()

