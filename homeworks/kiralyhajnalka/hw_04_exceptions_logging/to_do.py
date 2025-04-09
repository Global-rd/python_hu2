import logging
import os


logger = logging.getLogger('todo_logger')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('todo.log')
file_handler.setLevel(logging.DEBUG)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)

TASK_FILE = 'tasks.txt'


if not os.path.exists(TASK_FILE):
    open(TASK_FILE, 'w').close()

def read_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
        logger.info("Feladatok beolvasva.")
        return tasks
    except Exception as e:
        logger.error(f"Hiba a feladatok beolvasásánál: {e}")
        return []

def add_task(task):
    try:
        with open(TASK_FILE, 'a') as f:
            f.write(task + '\n')
        logger.info(f"Feladat hozzáadva: {task}")
    except Exception as e:
        logger.error(f"Hiba a feladat hozzáadásánál: {e}")

def remove_task(task):
    try:
        tasks = read_tasks()
        if task in tasks:
            tasks.remove(task)
            with open(TASK_FILE, 'w') as f:
                for t in tasks:
                    f.write(t + '\n')
            logger.info(f"Feladat törölve: {task}")
        else:
            logger.warning(f"A feladat nem található: {task}")
    except Exception as e:
        logger.error(f"Hiba a feladat törlésénél: {e}")

def display_menu():
    print("\nVálassz egy opciót:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Kérek egy számot:  ").strip()

        if choice == '1':
            task = input("Add meg a feladatot: ").strip()
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            print("\nFeladatok:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task = input("Add meg a törölendő feladat szövegét: ").strip()
            remove_task(task)
        elif choice == '4':
            logger.info("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás. ")

if __name__ == "__main__":
    main()
