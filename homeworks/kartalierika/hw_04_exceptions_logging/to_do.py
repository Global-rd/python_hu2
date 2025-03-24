import os
import logging

task_save = "tasks.txt"

#log fálj létrehozása
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),              
        logging.FileHandler("tasks.log")      
    ]
)

logger = logging.getLogger("task_logger")

#a gitignorban már megtalálható a log fájlokat kizáró kód

def display_menu():
    print("\nChoose an option:")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")

#feladat hozzáadása
def task_add(task):
    try:
        with open(task_save, "a", encoding="utf-8") as file:
            file.write(task + "\n")
        print("Task added:", task)
        logger.info(f"Task added: {task}")
    except Exception as e:
        print("Error while saving the task.")
        logger.error(f"Error writing to file: {e}")

#beolvasás
def task_read():
    try:
        if not os.path.exists(task_save):
            return []

        with open(task_save, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except Exception as e:
        print("Error while reading the tasks.")
        logger.error(f"Error reading from file: {e}")
        return []

#task törlése
def delete_task(task_to_delete):
    try:
        tasks = task_read()  
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            with open(task_save, "w", encoding="utf-8") as file:  
                for task in tasks:
                    file.write(task + "\n")
            print("Task removed:", task_to_delete)
            logger.info(f"Task removed: {task_to_delete}")
        else:
            print("Task not found.")
            logger.warning(f"Task not found: {task_to_delete}")
    except Exception as e:
        print("Error with deleting the task.")
        logger.error(f"Error while deleting the task: {e}")

#feladatkezelő
def main():
    while True:
        display_menu()
        choice = input("Which number do you choose? ")

        if choice == "1":
            task = input("Add a new task: ")
            task_add(task)
        elif choice == "2":
            tasks = task_read()
            if tasks:
                print("\nYour tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks found.")
        elif choice == "3":
            task = input("Enter the task you want to remove: ")
            delete_task(task)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4")



if __name__ == "__main__":
    main()

