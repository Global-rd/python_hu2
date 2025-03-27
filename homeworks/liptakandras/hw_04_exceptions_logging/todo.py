import os
import logging

todo = "homeworks/liptakandras/hw_04_exceptions_logging/todo.txt"
log_file = "homeworks/liptakandras/hw_04_exceptions_logging/todo.log"

file_handler = logging.FileHandler(log_file)
stream_handler = logging.StreamHandler()
formatter_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter_cons = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_cons)
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def view_tasks():
    try:
        with open(todo, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        logger.error(f"File not found: {todo}")

def add_task():
    try:
        with open(todo, "r") as file:
            lines = file.readlines()
            task_number = len(lines) + 1  # hozzáadódik
    except FileNotFoundError:
        task_number = 1  # ha nincs fájl, 1-est kap

    new_task = input("New task: ")
    try:
        with open(todo, "a") as file:
            file.write(f"{task_number}. {new_task}\n")  # hozzáadom a következő számmal
    except FileNotFoundError:
        logger.error(f"File not found: {todo}")  # ha nincs fájl

def remove_task():
    try:
        with open(todo, "r") as file:  # újra be kell olvasni a fájlt
            lines = file.readlines()
    except FileNotFoundError:
        logger.error(f"File not found: {todo}")
        return

    for index, line in enumerate(lines):  # számozom a sorokat
        print(f"{index + 1}. {line.strip()}")

    try:
        number_of_task_to_remove = int(input("Number of task you want to remove: "))
    except ValueError:
        logger.error("Invalid input. Please enter a number!")  # ha nem számot ad meg
        return

    if 1 <= number_of_task_to_remove <= len(lines):  # szám szerinti törlés feltétele
        del lines[number_of_task_to_remove - 1]  # törlés
        try:
            with open(todo, "w") as file:  # felülírom a listát
                file.writelines(lines)
            print(f"Task {number_of_task_to_remove} removed.")
        except FileNotFoundError:
            logger.error(f"File not found: {todo}")
    else:
        print("Invalid task number.")

options = {
    1: "Add new task",
    2: "View tasks",
    3: "Remove task",
    4: "Exit",
}

while True:  # végtelen loop, amíg az első 3 opció valamelyikét választom
    print("What would you like to do?")
    for key, value in options.items():  # mindig kilistázom az options key-value párjait
        print(f"{key}. {value}")
    try:
        todo_option = int(input("Add number of option: "))  # választhat todo_option-t
    except ValueError:
        continue  # vissza a loop elejére

    if todo_option == 1:
        add_task()
    elif todo_option == 2:
        view_tasks()
    elif todo_option == 3:
        remove_task()
    elif todo_option == 4:
        print("Exit to do list!")
        break
    