import logging
import os

# Logging beállítás
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

TASKS_FILE = ("homeworks/baloghpeter/hw_04_exceptions_logging/task.txt")

# Feladatok olvasása
def read_tasks():
    try:
        if not os.path.exists(TASKS_FILE):
            open(TASKS_FILE, 'w').close()
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nFeladatok:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nNincsenek feladatok.")
    except Exception as e:
        logging.error(f"Hiba a feladatok olvasásakor: {e}")

# Új feladat hozzáadása
def add_task(task):
    try:
        with open(TASKS_FILE, "a") as file:
            file.write(task + "\n")
        logging.info(f"Feladat hozzáadva: {task}")
    except Exception as e:
        logging.error(f"Hiba a feladat hozzáadásakor: {e}")

# Feladat törlése
def remove_task(task_number):
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1).strip()
            with open(TASKS_FILE, "w") as file:
                file.writelines(tasks)
            logging.info(f"Feladat törölve: {removed_task}")
        else:
            print("Érvénytelen feladat szám.")
    except Exception as e:
        logging.error(f"Hiba a feladat törlésekor: {e}")

# Menü megjelenítése
def display_menu():
    print("""
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
""")

def main():
    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ")
        
        if choice == "1":
            task = input("Írd be az új feladatot: ")
            add_task(task)
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            read_tasks()
            try:
                task_number = int(input("Írd be a törlendő feladat számát: "))
                remove_task(task_number)
            except ValueError:
                print("Érvénytelen bemenet, számot adj meg!")
        elif choice == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció, próbáld újra!")

if __name__ == "__main__":
    main()