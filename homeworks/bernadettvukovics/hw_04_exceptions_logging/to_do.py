import logging
import os

# Set up logging (console + file)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
    logging.StreamHandler(),  # Log to console
    logging.FileHandler("app.log")  # Log to file
])

TASK_FILE = os.path.join(os.path.dirname(__file__), "tasks.txt")  # TXT file for storing tasks


def display_menu():
    """Displays the main menu."""
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def read_tasks():
    """Reads tasks from the TXT file and returns them as a list."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as file:
            return file.readlines()
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []


def write_tasks(tasks):
    """Writes the updated task list back to the TXT file."""
    try:
        with open(TASK_FILE, "w") as file:
            file.writelines(tasks)
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")


def add_task():
    """Adds a new task to the TXT file."""
    task = input("Enter the task to add: ").strip()
    if task:
        try:
            with open(TASK_FILE, "a") as file:
                file.write(task + "\n")
            logging.info(f"Task added: {task}")
        except Exception as e:
            logging.error(f"Error adding task: {e}")
    else:
        logging.warning("Empty task cannot be added.")


def remove_task():
    """Removes a task by its text or number."""
    tasks = read_tasks()
    if not tasks:
        print("No tasks available to remove.")
        return

    print("\n--- Your Tasks ---")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.strip()}")

    choice = input("Enter the task number or text to remove: ").strip()

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1).strip()
            write_tasks(tasks)
            logging.info(f"Task removed: {removed_task}")
        else:
            logging.warning("Invalid task number.")
    else:
        if choice + "\n" in tasks:
            tasks.remove(choice + "\n")
            write_tasks(tasks)
            logging.info(f"Task removed: {choice}")
        else:
            logging.warning("Task not found.")


# Main program loop
while True:
    display_menu()
    choice = input("Please choose an option (1-4): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        tasks = read_tasks()
        if tasks:
            print("\n--- Your Tasks ---")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
            logging.info("Tasks successfully loaded.")
        else:
            logging.info("No tasks available.")
    elif choice == "3":
        remove_task()
    elif choice == "4":
        logging.info("Exiting the application.")
        break
    else:
        logging.warning("Invalid option, please choose between 1-4.")