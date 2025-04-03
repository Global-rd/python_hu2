import logging

# Logging konfiguráció
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('task_manager.log'),
                              logging.StreamHandler()])

TASKS_FILE = 'tasks.txt'

def read_tasks():
    """Feladatok olvasása a fájlból."""
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        logging.error(f"A fájl '{TASKS_FILE}' nem található.")
        return []
    except Exception as e:
        logging.error(f"Hiba történt a fájl olvasása közben: {e}")
        return []

def add_task(task):
    """Feladat hozzáadása a fájlhoz."""
    try:
        with open(TASKS_FILE, 'a') as file:
            file.write(task + '\n')
        logging.info(f"Feladat hozzáadva: {task}")
    except Exception as e:
        logging.error(f"Hiba történt a fájlba írás közben: {e}")

def remove_task(task_index):
    """Feladat törlése a fájlból."""
    tasks = read_tasks()
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        try:
            with open(TASKS_FILE, 'w') as file:
                for task in tasks:
                    file.write(task + '\n')
            logging.info(f"Feladat törölve: {removed_task}")
        except Exception as e:
            logging.error(f"Hiba történt a fájlba írás közben: {e}")
    else:
        logging.warning("Érvénytelen feladatindex.")

def display_menu():
    """Menü megjelenítése."""
    print("\nFeladatkezelő")
    print("1. Feladat hozzáadása")
    print("2. Feladatok megtekintése")
    print("3. Feladat törlése")
    print("4. Kilépés")

def main():
    """Főprogram."""
    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ")

        if choice == '1':
            task = input("Add meg a feladatot: ")
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            if tasks:
                print("\nFeladatok:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Nincsenek feladatok.")
        elif choice == '3':
            tasks = read_tasks()
            if tasks:
                print("\nFeladatok:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_index = int(input("Add meg a törlendő feladat sorszámát: "))
                    remove_task(task_index)
                except ValueError:
                    logging.warning("Érvénytelen bemenet. Számot adj meg.")
            else:
                print("Nincsenek feladatok.")
        elif choice == '4':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Kérlek, válassz 1 és 4 közötti számot.")

if __name__ == "__main__":
    # tasks.txt fájl létrehozása, ha nem létezik
    try:
        open(TASKS_FILE, 'x').close()
    except FileExistsError:
        pass  # A fájl már létezik

    main()