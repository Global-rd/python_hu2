import logging

possible_choices = ["1", "2", "3", "4"]

def add_task(input):
    if input:
        try:
            with open("tasks.txt", 'a') as file:
                file.write(f"{input}\n")
                file.close()
        except Exception as error:
            logging.error(f"An error accrued: {error}")
    else:
        logging.warning(f"Cannot add empty input to tasks")

def view_tasks():
    with open("tasks.txt", 'r') as file:
        content = file.readlines()
        file.close()
    if content == []:
        logging.warning(f"Tasks is empty.")
        return print("\nEmpty!")
    for number, line in enumerate(content, 0):
        print(f"\n{number}: {line.strip()}")
    
def remove_task(input):
    with open("tasks.txt", 'r') as file:
        content = file.readlines()
        file.close()
    if content == []:
        logging.warning(f"Tasks is empty.")
        return print("\nEmpty!")
    elif int(input) < 0 or int(input) > len(content):
        logging.warning(f"Invalid number.")
        return print("\nInvalid number!")
    for number, line in enumerate(content, 0):
        if int(input) == int(number):
            content.pop(number)
        file.close()
    with open("tasks.txt", 'w') as file:
        file.writelines(content)
        file.close()

def display_menu():
    print("\n1: Add Task:")
    print("2: View Task:")
    print("3: Remove Task:")
    print("4: Exit\n")

while True:
    display_menu()
    choice = str(input("Select an option: "))
    if choice in possible_choices:
        if choice == "1":
            user_input = input("\nType the name of the task you want to add: ")
            add_task(user_input)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            user_input = input("\nEnter the task number you want to remove: ")
            try:
                remove_task(user_input)
            except Exception as error:
                logging.error(f"An error accrued: {error}")
        elif choice == "4":
            logging.info("Closing program.")
            exit()
    else:
        print("\nInvalid number!")