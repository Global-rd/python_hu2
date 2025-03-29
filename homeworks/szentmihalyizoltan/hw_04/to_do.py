import logging

# Logging beállítások
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
])

# A feladat elérési útja
FILENAME  = 'hw_04/to_do.txt'

# Feladat olvasása
def view_task():
    try:
        with open(FILENAME , 'r') as file:            
            task = file.readlines()
        return task
    except FileNotFoundError:
        logging.warning(f"{file} nem található. Üres lista visszaadása.")
        return []
 
# Feladat hozzáadása  
def add_task(task):
    try:
        with open(FILENAME, 'a') as file:
             file.write(task)
    except FileNotFoundError:
        logging.warning(f"{file} nem található. Üres lista visszaadása.")

# Feladat törlése
def delete_task(task):
        try:
            with open(FILENAME, 'w') as file:
                for number, line in enumerate(task, 0):
                        task.pop(number)
                file.close()

        except FileNotFoundError:
            logging.warning(f"{file} nem található. Üres lista visszaadása.")
            return []

# Feladatok kiiratása
def display_menu():
    print("1. View task")
    print("2. Add task")
    print("1. Remove task")
    print("1. Exit")

# Main rész
def main():
    while True:
        try:
            display_menu()
            number = int(input("Add meg a feladat számát"))    
            if number == 1:
                view_task()
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
            print(f"Value error: {e}")

if __name__ == "__main__":
    main()