
import logging

# Set up logging to console and the log file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
    logging.StreamHandler(),  # Output to console
    logging.FileHandler("app.log")  # Output to log file
])

TASK_FILE = "tasks.txt"

#Display menu options
def display_menu():
    """Function to display the menu options."""
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Main loop for user interaction
while True:
    # Display menu
    display_menu()

    choice = input("Please choose an option (1-4): ").strip()

    if choice == "1":  # Add Task
        task = input("Enter the task to add: ").strip()
        if task:
            try:
                with open(TASK_FILE, "a") as file:
                    file.write(task + "\n")
                logging.info(f"Task '{task}' added successfully.")
            except Exception as e:
                logging.error(f"Error adding task: {e}")
        else:
            logging.warning("Empty task cannot be added.")

    elif choice == "2":  # View Tasks
        try:
            with open(TASK_FILE, "r") as file:
                tasks = file.readlines()
            if tasks:
                print("\n--- Your Tasks ---")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
                logging.info("Tasks successfully loaded.")
            else:
                logging.info("No tasks to display.")
        except FileNotFoundError:
            logging.error("Task file not found. Creating a new one.")

    elif choice == "3":  # Remove Task
        task_to_remove = input("Enter the task or number to remove: ").strip()
        
        if task_to_remove.isdigit():  # If the user entered a number
            try:
                with open(TASK_FILE, "r") as file:
                    tasks = file.readlines()
                task_index = int(task_to_remove) - 1
                if 0 <= task_index < len(tasks):  # Valid index
                    removed_task = tasks.pop(task_index)
                    with open(TASK_FILE, "w") as file:
                        file.writelines(tasks)
                    logging.info(f"Task '{removed_task.strip()}' removed successfully.")
                else:
                    logging.warning(f"Task number {task_to_remove} not found.")
            except Exception as e:
                logging.error(f"Error removing task by number: {e}")
        else:  # If the user entered a task name
            try:
                with open(TASK_FILE, "r") as file:
                    tasks = file.readlines()
                if task_to_remove + "\n" in tasks:
                    tasks.remove(task_to_remove + "\n")
                    with open(TASK_FILE, "w") as file:
                        file.writelines(tasks)
                    logging.info(f"Task '{task_to_remove}' removed successfully.")
                else:
                    logging.warning(f"Task '{task_to_remove}' not found.")
            except Exception as e:
                logging.error(f"Error removing task by name: {e}")

    elif choice == "4":  # Exit
        logging.info("Exiting the App.")
        break

    else:
        logging.warning("Invalid option, please choose between 1-4.")
