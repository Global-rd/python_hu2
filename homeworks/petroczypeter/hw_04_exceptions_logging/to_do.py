import os

# Define the relative path
relative_file_path = "homeworks/petroczypeter/hw_04_exceptions_logging/task_list.txt"

# Create an empty tasks file using context manager
with open(relative_file_path, "w") as file:
    pass  # Create empty file


# Add a new task to our file
def add_task(task):
    try:
        with open(relative_file_path, "a") as file:
            file.write(f"{task}\n")
        print(f"Following task has been added to our file: {task}")
    except Exception as e:
        print(f"Error adding task '{task}' to the file: {e}")


# View tasks in the file and add ID to it
def view_tasks():
    try:
        with open(relative_file_path, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("There are no tasks, Hawaii")
            return

        print("Task list:\n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
    except Exception as e:
        print(f"Error reading the tasks list: {e}")


# Remove task from the file if the entered task string matches a task in the list
def remove_task(task_to_be_removed):
    try:
        with open(relative_file_path, "r") as file:
            tasks = file.readlines()  # reading all tasks as a list

        if not tasks:  # if our file was empty
            print("No tasks to remove.")
            return

        task_found = False
        updated_tasks = []

        for task in tasks:
            if task.strip() == task_to_be_removed.strip():
                task_found = True
                print(f"Task '{task.strip()}' has been removed.")
            else:
                updated_tasks.append(task)

        # so this filtering pattern with the updated_tasks list was suggested by my LLM assistant.
        # Originally I wanted to use a remove, but then the remove() would've only deleted the first occurence
        # so then to ensure that we also delete in case of multiple occurences, I used a while loop
        # but then it become overcomplicated so I went with this code instead...

        if not task_found:
            raise ValueError(
                f"Task entered by user '{task_to_be_removed}' was not found, deletion cannot happen. AJJAJJ!"
            )

        # Now we write the updated tasks list back to the file
        with open(relative_file_path, "w") as file:
            file.writelines(updated_tasks)

    except Exception as e:
        print(f"error removing task: {e}")


def display_options():
    print("--==Task Manager==--")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit\n")


while True:
    display_options()

    try:
        selected_option = int(input("Please chose an option between 1 and 4: ").strip())

        if selected_option not in ["1", "2", "3", "4"]:
            raise ValueError(
                "Invalid user input. Please enter a number between 1 and 4."
            )

        if selected_option == 1:
            task = input("Enter the task to add: ").strip()
            add_task(task)

        elif selected_option == 2:
            view_tasks()

        elif selected_option == 3:
            task_to_be_removed = input("Enter the task to be removed: ").strip()
            remove_task(task_to_be_removed)

        elif selected_option == 4:
            print("Viszonlá")
            break

    except Exception as e:
        print(f"An unexpected error occured: {e}")
