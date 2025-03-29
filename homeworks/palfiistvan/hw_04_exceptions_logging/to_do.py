import os
import logging

text_file = "homeworks/palfiistvan/hw_04_exceptions_logging/feladat.txt"

file_handler = logging.FileHandler("homeworks/palfiistvan/hw_04_exceptions_logging/to_do.log")
stream_handler = logging.StreamHandler()
formatter_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter_cons = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_cons)
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def add_task(task):
    try:
        with open(text_file, "a") as file:
            file.write(task + "\n")
            print(f"{task} added")
    except FileNotFoundError:
        logger.error("Failed to save the task!")    
    print("\n------------------------------------\n")

def view_task():
    print("View tasks:\n")
    try:
        with open(text_file, "r") as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    print(line.strip())
            else:
                logger.error("The file is empty!")
    except FileNotFoundError:
        logger.error("The file does not exist!")
    print("\n------------------------------------\n")

def remove_task(task):
    try:
        with open(text_file, "r") as file:
            lines = file.readlines()
            if task + '\n' in lines:
                lines.remove(task + '\n')
                with open(text_file, 'w') as file:
                    file.writelines(lines)
                print(f"{task} deleted")
            else:
                logger.error("There is no such task!")
    except FileNotFoundError:
        logger.error("The file does not exist!")
    print("\n------------------------------------\n")

def display_menu():
    print("1. Add Task \n"
        "2. View Tasks \n"
        "3. Remove Task \n"
        "4. Exit \n")
    while True:
        chosen = int(input("Choose please: "))
        if chosen in range(1,5):
            if chosen %2 != 0:
                task = input("What is the task?: ")
            else:
                task = None
            return chosen, task
        logger.info("The selection must be between 1 and 4!")
        continue

def main():
    while True:
        chosen, task = display_menu()
        if int(chosen) == 1:
            add_task(task)
        elif int(chosen) == 2:
            view_task()
        elif int(chosen) == 3:
            remove_task(task)
        else:
            logger.info("Program RUN completed.")
            break

main()