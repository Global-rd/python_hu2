"""
Hozz létre egy új mappát a neveddel ellátott mappán belül
“hw_04_exceptions_logging” néven. A következő feladatokhoz tartozó .py file-okat ide mentsd el.
Feladat 1:
Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat megoldását:
Készíts egy Feladatkezelő alkalmazást!
Hozz létre egy .txt file-t és hagyd üresen.
● Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat hozzáadása, egy feladat törlése.
● Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok
közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es
vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a
megfelelő függvénynek. “Exit”-re lépjen ki a program.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a
logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. A .txt file
legyen része a pull request-nek, de a log file-ok ne! Használd a .gitignore-t!
"""

import os
import logging

# Logging beállítása (konzol + fájl)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log mentése fájlba
        logging.StreamHandler()  # Logolás konzolra
    ]
)

TASKS_FILE = "tasks.txt"  # Feladatok tárolására szolgáló fájl

def show_menu():
    """Megjeleníti a menüt."""
    print("\n--- Feladatkezelő ---")
    print("1. Új feladat hozzáadása")
    print("2. Feladatok megtekintése")
    print("3. Feladat törlése")
    print("4. Kilépés")

def load_tasks():
    """Betölti a feladatokat a fájlból."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except Exception as e:
        logging.error(f"Hiba a fájl olvasásakor: {e}")
        return []

def save_tasks(tasks):
    """Menteni a feladatokat a fájlba."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(tasks) + "\n")
    except Exception as e:
        logging.error(f"Hiba a fájl írásakor: {e}")

def add_task():
    """Új feladat hozzáadása."""
    task = input("Írd be a feladatot: ").strip()
    if task:
        try:
            with open(TASKS_FILE, "a", encoding="utf-8") as f:
                f.write(task + "\n")
            logging.info(f"Hozzáadott feladat: {task}")
        except Exception as e:
            logging.error(f"Hiba a feladat mentésekor: {e}")
    else:
        print("Üres feladat nem adható hozzá!")

def delete_task():
    """Feladat törlése."""
    tasks = load_tasks()
    if not tasks:
        print("Nincsenek feladatok.")
        return
    
    print("\n--- Feladataid ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    try:
        choice = int(input("Melyik feladatot szeretnéd törölni? (szám): "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            logging.info(f"Törölt feladat: {removed}")
        else:
            print("Érvénytelen szám.")
    except ValueError:
        print("Kérlek, számot adj meg!")

def main():
    """A fő program futtatása."""
    while True:
        show_menu()
        option = input("Válassz egy lehetőséget (1-4): ").strip()
        if option == "1":
            add_task()
        elif option == "2":
            tasks = load_tasks()
            if tasks:
                print("\n--- Feladataid ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Nincsenek mentett feladataid.")
        elif option == "3":
            delete_task()
        elif option == "4":
            logging.info("A program leáll.")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")

if __name__ == "__main__":
    main()
