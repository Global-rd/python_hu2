import os
import logging

# LOG CONFIG
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("task_manager.log"),
                        logging.StreamHandler()
                    ])

TASKS_FILE = 'tasks.txt'

def read_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except Exception as e:
        logging.error(f"Error reading tasks from file: {e}")
        return []

def add_task(task):
    try:
        with open(TASKS_FILE, 'a') as file:
            file.write(task + '\n')
            logging.info(f"Task added: {task}")
    except Exception as e:
        logging.error(f"Error adding task: {e}")

def remove_task(task_number):
    tasks = read_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        try:
            with open(TASKS_FILE, 'w') as file:
                file.writelines([task + '\n' for task in tasks])
                logging.info(f"Task removed: {removed_task}")
        except Exception as e:
            logging.error(f"Error removing task: {e}")
    else:
        logging.warning("Attempted to remove a task with an invalid number.")

def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            if tasks:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks found.")
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please select 1, 2, 3, or 4.")
    
if __name__ == "__main__":
    main()