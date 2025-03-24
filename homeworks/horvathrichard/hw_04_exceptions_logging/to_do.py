import os
import json  #json fimportálása az adatbáziskezeléshez
from setup_logger import setup_logger # a logging beállításokat szépen "kilopjuk" az órai anyagból 

logger = setup_logger('to_do')  # 

#---- a három függvény:
# feladatok olvasása:
def view_tasks():
    try:
        with open("homeworks/horvathrichard/hw_04_exceptions_logging/todo.json", "r", encoding = "utf-8") as file: # utf-8 kódolással (ékezetek,stb.) megnyitjuk a fájlt olvasásra
            tasks = json.load(file)   # a megnyitott fájl tartalmát meghatározzuk "tasks"-ként
            if tasks:
                for index, task in enumerate(tasks, start=1):  # feladatok indexelt kiírása a terminálra
                    print(f"{index}. {task}")
            else:
                print("Nincsenek feladatok.")
    except FileNotFoundError:               #-------------------------------------|
        logger.error("A lista nem található!")     #                              |
    except json.JSONDecodeError:     #                                            |
        logger.error("A fájl nem JSON formátumban van!")    #                     |------- HIBAKEZELÉS
    except Exception as e:    #                                                   |
        logger.error(f"Hiba történt a feladatok olvasása közben: {e}")    # ------|
    

# feladat hozzáadása:
def add_task(task):
    try:
        with open("homeworks/horvathrichard/hw_04_exceptions_logging/todo.json", "r+", encoding="utf-8") as file:
            tasks = json.load(file) 
            tasks.append(task) 

            with open("homeworks/horvathrichard/hw_04_exceptions_logging/todo.json", "w", encoding="utf-8") as write_file:
                json.dump(tasks, write_file, ensure_ascii=False, indent=4)   # a chatgpt-t kérdeztem hogyan kell a json fájlokat kezelni, azt írta hogy szükség van erre a sorra a mentéshez.
        logger.info(f"Feladat hozzáadva: {task}")                            # a "with open" nem felelős a fájl automatikus mentéséért is a bezáráson kívül? 
    except Exception as e:
        logger.error(f"Hiba történt a feladat hozzáadása közben: {e}")

# feladat törlése
def remove_task(task):
    try:
        with open("homeworks/horvathrichard/hw_04_exceptions_logging/todo.json", "r+", encoding="utf-8") as file:
            tasks = json.load(file)
        if task in tasks:
            tasks.remove(task)

            with open("homeworks/horvathrichard/hw_04_exceptions_logging/todo.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=4)  
            logger.info(f"Feladat törölve: {task}")
        else:
            logger.warning(f"A törlendő feladat nem található: {task}")
    except FileNotFoundError:
        logger.error("A lista nem található!")
    except json.JSONDecodeError:
        logger.error("A fájl nem JSON formátumban van!")
    except Exception as e:
        logger.error(f"Hiba történt a feladat törlése közben: {e}")

#---- a fő függvény, ami kezeli a fennti 3-at:
def display_menu():
    while True:
        print("\nFeladatkezelő alkalmazás")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        try:
            choice = int(input("Válassz egy opciót (1-4): "))
            if choice == 1:
                task = input("Add meg a hozzáadni kívánt feladatot: ")
                add_task(task)
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                task = input("Add meg a törölni kívánt feladatot: ")
                remove_task(task)
            elif choice == 4:
                logger.info("Kilépés a programból.")
                print("Kilépés...")
                break
            else:
                logger.warning("Érvénytelen választás történt.")
                print("Érvénytelen választás! Kérlek válassz 1 és 4 között.")
        except ValueError:
            logger.warning("Érvénytelen bevitel történt. A felhasználó nem számot adott meg.")
            print("Kérlek érvényes számot adj meg (1-4).")

# a program közvetlenül fut:
if __name__ == "__main__":
    display_menu()
