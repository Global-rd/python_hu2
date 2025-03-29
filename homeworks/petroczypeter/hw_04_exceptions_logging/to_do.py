import logging
import json  # adding this for the extra task

# the 4 steps of logging setup:

# 1. create handlers - where the logs will go
file_handler = logging.FileHandler("todo_app.log")
stream_handler = logging.StreamHandler()

# 2. Define the formatter - how the logs will look
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# 3. Assigning the formatter to each handler
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 4. Creating logger and assign the handlers to it
logger = logging.getLogger("todo_app")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Define the relative path
relative_file_path = "homeworks/petroczypeter/hw_04_exceptions_logging/task_list.json"

# Create an empty tasks file using context manager
try:
    with open(relative_file_path, "w") as file:
        json.dump([], file)  # initialize with an empty list
    logger.info(
        f"Created empty task file at: {relative_file_path}"
    )  # Log when file is created

except Exception as e:
    logger.error(
        f"Error creating task file: {e}"
    )  # Log errors while tryint to create file


# Add a new task to our file
def add_task(task):
    try:
        tasks = []
        try:
            with open(relative_file_path, "r") as file:
                tasks = json.load(file)  # read the existing tasks from the JSON
        except (FileNotFoundError, json.JSONDecodeError):
            # The file doesn't exist or it's empty or it's invalid then we start with an empty list
            tasks = []

        # Add the new task
        tasks.append(task)

        # Write the entire list back to the file
        with open(relative_file_path, "w") as file:
            json.dump(tasks, file, indent=2)  # indentation for readability

        print(f"Following task has been added to our file: {task}")
        logger.info(f"Task added: '{task}'")  # Log task addition

    except Exception as e:
        error_msg = f"Error adding task '{task}' to the file: {e}"
        print(error_msg)
        logger.error(error_msg)  # Log errors while trying to add a task


# View tasks in the file and add ID to it
def view_tasks():
    try:
        with open(relative_file_path, "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("There are no tasks, Hawaii")
            logger.info(
                "User opened the tasks, but there weren't any, they can go to Hawaii"
            )  # Log that tasks are not found
            return

        print("Task list:\n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
        logger.info(f"User viewed {len(tasks)} tasks")  # Log how many tasks were viewed

    except FileNotFoundError:  # if the file doesn't exist yet
        error_msg = "Task file not found. No tasks to display."
        print(error_msg)
        logger.error(error_msg)
    except json.JSONDecodeError as e:  # if the file contains invalid JSON
        error_msg = f"Error parsing JSON data: {e}"
        print(error_msg)
        logger.error(error_msg)
    except Exception as e:  # general exceptions
        error_msg = f"Error reading the tasks list: {e}"
        print(error_msg)
        logger.error(error_msg)


# Remove task from the file if the entered task string matches a task in the list
def remove_task(task_to_be_removed):
    try:
        with open(relative_file_path, "r") as file:
            tasks = json.load(file)

        if not tasks:  # if our file was empty
            print("No tasks to remove.")
            logger.info("User tried to remove a task but the file was empty")
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
            error_msg = f"Task entered by user '{task_to_be_removed}' was not found, deletion cannot happen. AJJAJJ!"
            logger.warning(error_msg)  # Logging a warning as nothing was found
            raise ValueError(error_msg)

        # Now we write the updated tasks list back to the file
        with open(relative_file_path, "w") as file:
            json.dump(updated_tasks, file, indent=2)

        logger.info(
            f"Removed '{task_to_be_removed}' from the list"
        )  # I do have some second thoughts on this... Isn't this too chatty to log down what was actually deleted? Isn't that kind of a data leakage?

    except FileNotFoundError:
        error_msg = "Task file not found. No tasks to remove."
        print(error_msg)
        logger.error(error_msg)
    except json.JSONDecodeError as e:
        error_msg = f"Error parsingn JSON data: {e}"
        print(error_msg)
        logger.error(error_msg)
    except ValueError as e:
        print(e)
    except Exception as e:
        error_msg = f"error removing task: {e}"
        print(error_msg)
        logger.error(error_msg)  # Log error while tryint to remove


def display_options():
    print("--==Task Manager==--")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit\n")


logger.info("Task Manager Python app started. Yay!")

while True:
    display_options()

    try:
        selected_option = int(input("Please chose an option between 1 and 4: ").strip())

        if selected_option not in [1, 2, 3, 4]:
            error_msg = "Invalid user input. Please enter a number between 1 and 4."
            logger.warning(f"Invalid menu option selected: {selected_option}")
            raise ValueError(error_msg)

        if selected_option == 1:
            task = input("Enter the task to add: ").strip()
            logger.debug(
                f"User selected option 1: Add Task - '{task}'"
            )  # same question. Is this too chatty perhaps? Polluting logs with sensitive data?
            add_task(task)

        elif selected_option == 2:
            logger.debug("User selected option 2: View Tasks")
            view_tasks()

        elif selected_option == 3:
            task_to_be_removed = input("Enter the task to be removed: ").strip()
            logger.debug(
                f"User selected option 3: Remove task - '{task_to_be_removed}'"
            )
            remove_task(task_to_be_removed)

        elif selected_option == 4:
            print("Viszonlá")
            logger.info(
                "User selected option 4: Exit - Task Manager application shutting down, bye bye"
            )
            break

    except ValueError as e:
        if "invalid literal for int" in str(e):
            print("Invalid input. Please enter a number.")
            logger.warning("User doesn't know what is a number between 1-4")
        else:
            print(e)

    except Exception as e:
        error_msg = f"An unexpected error occured: {e}"
        print(error_msg)
        logger.error(error_msg)

# Log shutdown
logger.info("Task Manager application closed successfully.")
