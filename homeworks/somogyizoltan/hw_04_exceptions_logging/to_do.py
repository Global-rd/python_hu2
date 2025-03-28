"""
Készíts egy Feladatkezelő alkalmazást!
Hozz létre egy .txt file-t és hagyd üresen.
● Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat
hozzáadása, egy feladat törlése.
● Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges
opciókat:
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

# importálni a modulokat
import os
import logging
import setup_logger
# import datetime as dt


# LOGOLÁSHOZ

logger = setup_logger.setup_logger("root_logger")

logger.info("This is our first logging message -  Kezdődik a todo list program futása")

# Ez a loggolás még nem igazán tiszta, ezért átvettem az órai .py file-t a deklaráláshoz, csak kiegészítettem a saját könytárba mutató log file nevével
# Elsőre a felhasználói bemeneteket fogom INFO szintjén beírni (magyarul), aztán a file műveleteket is (hozzáadás és törlés), hogy tisztább legyen a kép
# Ez azért a mostani feladathoz túlságosan sok, de egy jó alap lesz, ha felhasználói futás közbeni hibákat kell tesztelni, felderíteni .....

# text file neve, amibe mentem az adatokat
td_file_name = "homeworks/somogyizoltan/hw_04_exceptions_logging/to_do_list_text_file.txt"

# Fő menü kiíratása, amit ciklusban fogok hívni
def display_menu():
    print("Please enter your choice!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# GENERATOR TO READ A FILE   - az órai anyagból vettem
def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line

# Hozzáadni egy új elemet a listához
def add_new_task(new_act):

    # Eredeti CM-mel ez a megoldás  
    #    with open(td_file_name, "a") as file:
    #        file.write(f"Activity: {new_act} \n")

    # Nem használom CM-t, hogy a hibakezelést is bele tudjam írni, és loggolni

    file = open(td_file_name, "a")
    try:
        file.write(f"Activity: {new_act} \n")
        # LOGGOLÁS
        logger.info(f"A {new_act} aktivitás hozzáadva a listához")
    finally:
        file.close()    


# Elvenni egy elemet a listából
def remove_one_task(num_act):
    
    # Tesztelni a bejövő adatot, hogy szám-e
    try:
        if int(num_act) == 0:
            print(f"{num_act} is wrong number for deleting!")
            logger.info(f"A törléshez megadott érték {num_act} nulla")
            
    except ValueError as e:
        print(f"{num_act} is not number for deleting! {e}")
        logger.info(f"A törléshez megadott érték {num_act} nem szám {e}")
        
    else:
        # Teszt rendben
        # Beolvasom egy listába a sorokat, kivéve a törlendő sort
        row_number = 0
        act_list = []
        
        for line in read_file_line_by_line(file_path=td_file_name):
            if row_number != int(num_act) or row_number == 0:
                act_list.append(line)
            row_number += 1   

        # Nem fut hibára, ha nagyobb számot ad meg a felhasználó, mint amennyi sor van a file-ban, de ezt loggolom
        if row_number <= int(num_act):
            logger.info(f"A {num_act} szám nagyobb, mint ahány elem van a file-ban.")
        

        # Létrehozni egy üres file-t
        with open(td_file_name, "w") as file: 
                
            file.write("")  
        #    file.close()          
        # Eredetileg ezek a file.close függvények is benne voltak, de láttam az egyik kollégának írt megjegyzésedet, hogy ezek feleslegesek

        with open(td_file_name, "a") as file: 
            # Visszaírni ebbe az üres, de azonos nevű file-ba a listából a sorokat      
            for line in act_list:
                file.write(line)
                            
        # file.close()
            
    

# Kiírni az elemeket a listából, az aktivitásokat sorszámozva, hogy a törlésnél egyértelmű legyen, hogy mit szeretne kitörölni
def view_all_tasks():
    row_number = 0
    for line in read_file_line_by_line(file_path=td_file_name):
        if row_number == 0:
            print(line)
        else:
            print(f"{row_number}. {line}")
            
        row_number += 1        


# Létrehozom a text file-t a fejléccel 
with open(td_file_name, "w") as file:
        file.write(f"ToDo list for today : \n")


# Main loop az menü kiíratására és az adatok bekérésehez

while True:
    display_menu()

    user_choice = int(input("Your choice is: "))

    # LOGGOLÁS
    logger.info(f"A felhasználó ezt a menüpontot adta meg: {user_choice}")

    if user_choice in range(1, 5):

       if user_choice == 4:         # Kilépés a programból
           break
       elif user_choice == 3:       # Elvenni egy elemet
           # Melyik sort szeretné törölni
           num_activity = input("Please, write the number of line for deleting: ")
           # LOGGOLÁS
           logger.info(f"A felhasználó ezt a számú {num_activity} sort akarja törölni")
           remove_one_task(num_act=num_activity)
       elif user_choice == 2:       # Listázni az összes elemet
           view_all_tasks()
       else:                        # Új elemet a lista végére tenni
           # bekérem az új sort
           new_activity = input("Please, write your new activity: ")
           # LOGGOLÁS
           logger.info(f"A felhasználó ezt a aktivitást {new_activity} szeretné hozzáadni")
           add_new_task(new_act=new_activity)
    else:
        print(f"Wrong number {user_choice}! Please try again!")

