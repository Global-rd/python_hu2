import logging # Logging module import
import os # OS module import

# Logging settings
log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file_path),
    logging.StreamHandler()
])

# MENU
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")



# Add task function
def add_task(file_name, task):
    try:
        with open(file_name, 'a') as file:
            file.write(task + '\n')
        logging.info(f"Added task: {task}")
    except Exception as e:
        logging.error(f"An error occurred when adding the task: {e}")

# Delete task function
def remove_task(file_name, task):
    try:
        tasks = read_tasks(file_name)
        if task in tasks:
            tasks.remove(task)
            with open(file_name, 'w') as file:
                for t in tasks:
                    file.write(t + '\n')
            logging.info(f"Deleted task: {task}")
        else:
            logging.warning(f"The task doesn't exist: {task}")
    except Exception as e:
        logging.error(f"An error occoured when deleting the task: {e}")

# Task reading function
def read_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        logging.error("The file doesn't exist.")
        return []

# Main function
def main():
    file_name = os.path.join(os.path.dirname(__file__), 'tasks.txt')
    while True:
        display_menu()
        choice = input("Choose an option (1, 2, 3, 4): ")
        if choice == '1':
            task = input("Add a task: ")
            add_task(file_name, task)
        elif choice == '2':
            tasks = read_tasks(file_name)
            print("Tasks:")
            for task in tasks:
                print(f"- {task}")
        elif choice == '3':
            task = input("Enter the task to be deleted: ")
            remove_task(file_name, task)
        elif choice == '4':
            print("Exit...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
 
 main()