import logging

# Logging beállítások
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
])

# A feladat elérési útja
FILENAME = 'homeworks/szentmihalyizoltan/hw_04/to_do.txt'

# Feladat olvasása
def view_task():
    try:
        with open(FILENAME, 'r') as file:            
            task = file.readlines()
        return task
    except FileNotFoundError:
        logging.warning(f"{FILENAME} nem található. Üres lista visszaadása.")
        return []

# Feladat hozzáadása  
def add_task(task):
    try:
        with open(FILENAME, 'a') as file:
             file.write(task + '\n')  # Új feladat új sorba kerüljön
    except FileNotFoundError:
        logging.warning(f"{FILENAME} nem található.")

# Feladat törlése
def delete_task(task_to_remove):
    try:
        tasks = view_task()  # Az összes feladatot beolvassuk
        if task_to_remove + '\n' in tasks:
            tasks.remove(task_to_remove + '\n')  # Ha benne van a listában, töröljük
            with open(FILENAME, 'w') as file:
                file.writelines(tasks)  # Az új listát visszaírjuk a fájlba
            logging.info(f"Feladat törölve: {task_to_remove}")
        else:
            logging.warning(f"A törlendő feladat nem található: {task_to_remove}")
    except FileNotFoundError:
        logging.warning(f"{FILENAME} nem található.")

# Feladatok kiiratása
def display_menu():
    print("1. View task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Main rész
def main():
    while True:
        try:
            display_menu()
            number = int(input("Add meg a feladat számát: "))    
            if number == 1:
                tasks = view_task()
                print("Feladatok:")
                for task in tasks:
                    print(task.strip())
            elif number == 2:
                task_input = input("Add meg a hozzáadni kívánt feladatot: ")
                add_task(task_input)
            elif number == 3:
                task_input = input("Add meg a törölni kívánt feladatot: ")
                delete_task(task_input)
            elif number == 4:
                break            
            else:
                print("Nem megfelelő tartomány, kérlek válassz 1 és 4 között")
        except ValueError as e:
            print(f"Érvénytelen bemenet: {e}")

if __name__ == "__main__":
    main()