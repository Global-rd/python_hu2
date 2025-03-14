import os
print(os.getcwd())

#Definiálj 3 függvényt a következőkre: 
#egy feladat hozzáadása
def _1add_task(file_path):
    while True:
        task = input("Adj hozzá új feladatot:").strip()
        if task == "":
            print("Ez nem sikerült. Próbáld meg újra.")

        else:
            try:
                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(task + "\n")
                    print("Sikeresen hozzáadtad az új feladatot!")
                    break
            except OSError as e:
                print("Hiba történt")
                continue
#--------------------------------------------------------------------------------
#feladatok olvasása
def _2read_task(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print("Nem találom a fájlt.")
        yield from iter([])
#--------------------------------------------------------------------------------
##egy feladat törlése
def _3delete_task(file_path, task):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    
        deleted = False
        with open(file_path, "w", encoding="utf-8") as file:
            for line in lines:
                if line.strip() != task:
                    file.write(line)
            
                else:
                    deleted = True #Törölés jelzésére
        if deleted:
            print(f'Sikeresen törölve: {task}!')
        else:
            print(f'Nem találtam ilyen feladatot: {task}!')
    except FileNotFoundError:
        print("Nem találom a fájlt.")
    except OSError as e:
        print(f"Hiba történt: {e}!")

#--------------------------------------------------------------------------------
"""
Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
"""

def display_menu():
    print("1. Add Task \n"
        "2. View Tasks \n"
        "3. Remove Task \n"
        "4. Exit \n")

   