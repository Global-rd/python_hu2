import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
file_handler = logging.FileHandler("to_do.log", encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
feladatok = "feladatok.txt"


if not os.path.exists(feladatok):
    try:
        with open(feladatok, "w", encoding="utf-8") as f:
            pass
    except Exception as e:
        logger.error(f"Error {feladatok} : {e}")

def read_tasks(feladatok):
    try:
        with open(feladatok, "r", encoding="utf-8") as f:
            tasks = f.readlines()
            tasks = [task.strip() for task in tasks if task.strip()]
        logger.info("Tasks added.")
        return tasks
    except Exception as e:
        logger.error(f"Error: {e}")
        return []

def add_task(file_name, task):
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(task + "\n")
        logger.info(f"Task added: {task}")
    except Exception as e:
        logger.error(f"Error: {e}")

def remove_task(file_name, task_to_remove):
    try:
        tasks = read_tasks(file_name)
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            with open(file_name, "w", encoding="utf-8") as f:
                for task in tasks:
                    f.write(task + "\n")
            logger.info(f"Task removed: {task_to_remove}")
        else:
            logger.info("Error.")
    except Exception as e:
        logger.error(f"Error: {e}")

def display_menu():
    print("\nFeladatkezelő")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Opt:(1, 2, 3, 4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Error, only 1, 2, 3, 4")
            continue

        if choice == '1':
            task = input("Add task: ")
            add_task(feladatok, task)
        elif choice == '2':
            tasks = read_tasks(feladatok)
            if tasks:
                print("\nFeladatok:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No task")
        elif choice == '3':
            task = input("Which task: ")
            remove_task(feladatok, task)
        elif choice == '4':
            print("Exit")
            break

if __name__ == "__main__":
    main()