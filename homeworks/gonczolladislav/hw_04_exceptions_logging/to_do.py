import os
import logging

print(os.getcwd())

# logging
file_handler = logging.FileHandler("logfile.log", encoding="utf-8")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

#logger.debug("Debug message")
#logger.info("Info message")
#logger.warning("Warning message")
#logger.error("Error message")
#logger.critical("Critical message")

def create_file_handler(log_file, level):
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    return file_handler

def create_stream_handler(level):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    return stream_handler

def set_formatter(handler):
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
    handler.setFormatter(log_format)

def setup_logger(name, log_file='logfile.log', level=logging.DEBUG, handlers=None):

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if handlers is None:
        handlers = ['file', 'stream']

    for handler in handlers:
        if handler == 'file':
            file_handler = create_file_handler(log_file=log_file, level=level)
            set_formatter(file_handler)
            logger.addHandler(file_handler)
        elif handler == 'stream':
            stream_handler = create_stream_handler(level)
            set_formatter(stream_handler)
            logger.addHandler(stream_handler)
    return logger

# setting a file name as constant
FILE_NAME = "to_do_list.txt" 

# add task
def add_task(task_description):
    
    if not task_description: 
        logger.warning("The task description cannot be empty.") 
        print("The task description cannot be empty.")
        return
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:          
            file.write(task_description + '\n')
        logger.info(f"Task added: '{task_description}'")
        print(f"Task added: '{task_description}'")
    except IOError as e:
        logger.error(f"File writing error: {e}")
        print(f"File writing error: {e}")
    except Exception as e:
        logger.critical(f"Failed to add task. Unexpected error : {e}")
        print(f"Failed to add task. Unexpected error : {e}")

#reading tasks
def read_tasks():
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                logger.warning(f"\nNo tasks found in file {FILE_NAME}.")
                print(f"\nNo tasks found in file {FILE_NAME}.")
                return [] 
            print("\n--- Task list ---")
            
            for index, line in enumerate(lines):
                print(f"{index + 1}. {line.strip()}")
            print("--------------------")
            return lines
    except FileNotFoundError:
        logger.error(f"\nA '{FILE_NAME}' file not exist. Please add a task to create the file.")
        print(f"\nA '{FILE_NAME}' file not exist. Please add a task to create the file.")
        return [] 
    except IOError as e:
        logger.error(f"File read error: {e}")
        print(f"File read error: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected read error: {e}")
        print(f"Unexpected read error: {e}")
        return []

#delete task
def delete_task():
    
    tasks = read_tasks() 
    if not tasks:
        if os.path.exists(FILE_NAME): 
            logger.info(f"{FILE_NAME} is empty. There is nothing to delete.") 
            print(f"{FILE_NAME} is empty. There is nothing to delete.")
        return 

    while True:
        try:            
            choice_str = input(f"Enter the number of the task you want to delete : (1-{len(tasks)}), or 'c' for cancel : ")
            if choice_str.lower() == "c":
                logger.info("Delete task is cancelled.")
                print("Delete task is cancelled.")
                return

            choice = int(choice_str)
            if 1 <= choice <= len(tasks):                              
                task_to_delete = tasks.pop(choice - 1).strip()               
                try:                    
                    with open(FILE_NAME, "w", encoding="utf-8") as file:                       
                        file.writelines(tasks)
                    logger.info(f"The task '{task_to_delete}' deleted successfully.")    
                    print(f"The task '{task_to_delete}' deleted successfully.")
                    break 
                except IOError as e:
                    logger.error(f"File write error: {e}")
                    print(f"File write error: {e}")                   
                    return 
                except Exception as e:
                    logger.error(f"Unexpected error occurred: {e}")
                    print(f"Unexpected error occurred: {e}")
                    return

            else:                
                logger.warning(f"Invalid task number. Please, enter number between 1  and {len(tasks)}.")
                print(f"Invalid task number. Please, enter number between 1  and {len(tasks)}.")
        except ValueError:          
            logger.error("Invalid input. Please choosse a number.")
            print("Invalid input. Please choosse a number.")
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            print(f"Unexpected error occurred: {e}")
            return    

#menu items
def display_menu():

    print("\n\n1. Add Task\n")
    print("2. View Tasks\n")
    print("3. Remove Task\n")
    print("4. Exit\n")
    print("______________________")

    while True:
        try:
            choice = int(input("Please choose one menu item from 1 to 4: "))
            if 1 <= choice <= 4:
                return choice 
            else:
                logger.warning("Invalid choice, please choose 1 to 4.")
                print("Invalid choice, please choose 1 to 4.")
        except ValueError:
            logger.error(("Invalid choice.Please add a number 1 to 4.") )
            print("Invalid choice.Please add a number 1 to 4.") 

        
def main():
    
    print("Welcome in To Do List App")
    print(f"(Working directory: {os.getcwd()})")
    print(f"Tasks will be saved to '{FILE_NAME}'.")

    while True:
        choice = display_menu() 
        if choice == 1:
            task_description = input("Add a new task: ")
            add_task(task_description.strip())
        elif choice == 2:
            read_tasks() 
        elif choice == 3:
            delete_task() 
        elif choice == 4:
            print("\nBye!")
            break 

if __name__ == "__main__":
    main()