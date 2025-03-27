import os
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler("app.log")
                    ])
logger = logging.getLogger()

filename = "bogi_hw_04.txt"

def read_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except Exception as e:
        logger.error(f"Hiba történt: {e}")
        return []

def add_task(task, filename):
    try:
        with open(filename, 'a') as file:
            file.write(task + "\n")
        logger.info(f"Feladat hozzáadva, ahogy kérted.")
    except Exception as e:
        logger.error(f"Hiba történt: {e}")

def remove_task(task, filename):
    try:
        tasks = read_tasks(filename)
        if task in tasks:
            tasks.remove(task)
            with open(filename, 'w') as file:
                for task in tasks:
                    file.write(task + "\n")
            logger.info(f"Feladat törölve, ahogy kérted.")
        else:
            logger.warning("A törlendő feladat nem létezik.")
    except Exception as e:
        logger.error(f"Hiba történt: {e}")

def display_menu():
    print("\nFeladatkezelő menü:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def get_valid_input():
    while True:
        choice = input("Válaszd ki egy opciót a menüből. Válaszod egy szám legyen 1, 2, 3 és 4 között: ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            logger.warning("Érvénytelen opció! Válaszod egy szám legyen 1, 2, 3 és 4 között.")

def main():
    
    
    while True:
        display_menu()
        choice = get_valid_input()

        if choice == "1":
            task = input("Add meg a feladat nevét amit a listára akarsz írni: ")
            add_task(task, filename)
        elif choice == "2":
            tasks = read_tasks(filename)
            if tasks:
                print("\nAktuális feladatok a listán:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}"),
                logger.info(f"Feladatlista kimutatva")
            else:
                logger.info(f"Nincsenek feladatok.")
        elif choice == "3":
            task = input("Add meg a törlendő feladatot: ")
            remove_task(task, filename)
        elif choice == "4":
            logger.info(f"Kilépés a programból")
            break

if __name__ == "__main__":
    main()
