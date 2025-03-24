def display_menu():
    menu_options = ["1) Add task", "2) View task", "3) Remove task", "4) Exit"]
    for option in menu_options:
        print(option)

def add_task():
    new_task = input("What task would you like to add? ")
    try:
        with open("tasks.txt", "a") as f:
            f.write(new_task + "\n")
        print("Task added.")
    except Exception:
        print("Error adding task.")

def view_task():
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except Exception:
        print("Error reading tasks.")

def delete_task():
    task_to_delete = input("What task would you like to remove? ")
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()

        kept_lines = []
        for line in lines:
            if line.strip() != task_to_delete:
                kept_lines.append(line)

        with open("tasks.txt", "w") as f:
            for line in kept_lines:
                f.write(line)

        print("Task removed (if it existed).")
    except Exception:
        print("Error removing task.")

def task_manager():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid number, choose only from 1-4, idiot!")

if __name__ == "__main__":
    task_manager()