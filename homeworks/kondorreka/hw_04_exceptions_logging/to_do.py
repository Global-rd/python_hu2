import os
from to_do_def import _1add_task #1. Add Task
from to_do_def import _2read_task #2. View Tasks
from to_do_def import _3delete_task #3. Remove Task
from to_do_def import display_menu #kiprinteli a lehetséges opciókat
import logging

#Mappák létrehozása, ha nem léteznek
data_dir = "kondorreka/data"
logs_dir = "kondorreka/logs"
os.makedirs(data_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# Készíts egy Feladatkezelő alkalmazást!
# Hozz létre egy .txt file-t és hagyd üresen.

print(os.getcwd())

file_path = os.path.join(data_dir, "hw_04.txt")

if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        pass  # Üres fájl létrehozása

print(f"A fájl abszolút elérési útja: {os.path.abspath(file_path)}")

file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

logger.info("A program elindult.")

# Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok
# közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.

display_menu()

while True:
    command = input("Adj meg egy számot, és indulhat a varázslat! ")
    try:
        command = int(command)
        if command not in range(1,5):
            print(f"A {command} sajnos nem egy varázslatos lehetőség. Próbáld meg újra!")
            logger.warning(f"Érvénytelen parancs: {command}")
            continue
     
        elif command == 1:
            _1add_task(file_path)
            logger.info("Feladat hozzáadva.")
        elif command == 2:
            for task in _2read_task(file_path):
                print(task)
            logger.info("Feladatok megtekintve.")
        elif command == 3:
            task = input("Melyik feladat törölhető? ")
            _3delete_task(file_path, task)
            logger.info(f"Feladat törölve: {task}")
        else:
            print("Legyen szép napod!")
            break
    except ValueError:
        print("Hoppá! Csak számot adhatsz meg 1-4-ig. Próbáld meg újra!")
        logger.error("Érvénytelen bemenet! Szám helyett más karakter lett megadva.")