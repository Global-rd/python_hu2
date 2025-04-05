import logging

logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s [%(levelname)s] %(message)s", 
                    handlers=[logging.FileHandler("to_do.log"), logging.StreamHandler()])

def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

FILE_PATH = "/Users/beresnikolett/Documents/python_rd_repo/python_hu2/homeworks/beresnikolett/hw_04_exeptions_logging/tasks.txt"

def add_task(task, filename=FILE_PATH):
    try:
        with open(filename, "a") as file:
            file.write(task + "\n")
        logging.info(f"Task added: {task}")
    except Exception as e:
        logging.error(f"Error while adding task: {e}")

def view_tasks(filename=FILE_PATH):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except Exception as e:
        logging.error(f"Error while viewing tasks: {e}")
        return []

def remove_task(task, filename=FILE_PATH):
    try:
        tasks = view_tasks(filename)
        if task in tasks:
            tasks.remove(task)
            logging.info(f"Task removed: {task}")
            with open(filename, "w") as file:
                for task in tasks:
                    file.write(task + "\n")  
        else:
            logging.warning(f"Task not found: {task}")
    except Exception as e:
        logging.error(f"Error while removing task: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task, filename=FILE_PATH)

        elif choice == "2":
            tasks = view_tasks()
            for task in tasks:
                print(f"Task: {task}")

        elif choice == "3":
            task_to_remove = input("Enter task to remove: ")
            remove_task(task_to_remove, filename=FILE_PATH)

        elif choice == "4":
            print("Exiting the program.")
            break
            return
        else:
            print("Invalid choice. Please try again (1-4).")


main()